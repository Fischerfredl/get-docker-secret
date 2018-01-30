import os
import unittest
from get_docker_secret import get_docker_secret


class TestSecrets(unittest.TestCase):
    """Not tested under windows"""

    secrets_dir = os.path.dirname(os.path.realpath(__file__))

    def write_secret(self, name, value):
        with open(os.path.join(self.secrets_dir, name), 'w') as file:
            file.write(value)

    def remove_secret(self, name):
        os.remove(os.path.join(self.secrets_dir, name))

    def setUp(self):
        self.write_secret('my_key', 'my_value')
        self.write_secret('my_int_key', '5')
        self.write_secret('my_float_key', '5.4')
        self.write_secret('my_bool_key_true', 'true')
        self.write_secret('my_bool_key_false', 'false')
        self.write_secret('UPPER_CASE_KEY', 'my_value')

    def tearDown(self):
        self.remove_secret('my_key')
        self.remove_secret('my_int_key')
        self.remove_secret('my_float_key')
        self.remove_secret('my_bool_key_true')
        self.remove_secret('my_bool_key_false')
        self.remove_secret('UPPER_CASE_KEY')

    def test_normal(self):
        value = get_docker_secret('my_key', secrets_dir=self.secrets_dir)

        self.assertEqual(value, 'my_value')

    def test_default(self):
        value = get_docker_secret('invalid', secrets_dir=self.secrets_dir)
        self.assertIsNone(value)

        value = get_docker_secret('invalid', default='a_value', secrets_dir=self.secrets_dir)
        self.assertEqual(value, 'a_value')

        value = get_docker_secret('invalid', default='None', secrets_dir=self.secrets_dir)
        self.assertEqual(value, 'None')

    def test_cast(self):
        value = get_docker_secret('my_int_key', cast_to=int, secrets_dir=self.secrets_dir)
        self.assertIsInstance(value, int)
        self.assertEqual(value, 5)

        value = get_docker_secret('my_float_key', cast_to=float, secrets_dir=self.secrets_dir)
        self.assertIsInstance(value, float)
        self.assertEqual(value, 5.4)

        value = get_docker_secret('my_bool_key_true', cast_to=bool, secrets_dir=self.secrets_dir)
        self.assertIsInstance(value, bool)
        self.assertTrue(value)

        value = get_docker_secret('my_bool_key_false', cast_to=bool, secrets_dir=self.secrets_dir)
        self.assertIsInstance(value, bool)
        self.assertFalse(value)

    def test_cast_fail(self):
        with self.assertRaises(ValueError):
            get_docker_secret('my_bool_key_true', cast_to=int, safe=False, secrets_dir=self.secrets_dir)

        with self.assertRaises(ValueError):
            get_docker_secret('my_int_key', cast_to=bool, safe=False, secrets_dir=self.secrets_dir)

    def test_autocast_name(self):
        value = get_docker_secret('MY_KEY', autocast_name=True, secrets_dir=self.secrets_dir)
        self.assertEqual(value, 'my_value')

        # assumes case-sensitiveness of os. could fail on windows
        value = get_docker_secret('MY_KEY', autocast_name=False, secrets_dir=self.secrets_dir)
        self.assertIsNone(value)

    def test_safe_not_found(self):
        value = get_docker_secret('invalid', safe=True, secrets_dir=self.secrets_dir)
        self.assertIsNone(value)

        with self.assertRaises(TypeError):
            get_docker_secret('invalid', safe=False, secrets_dir=self.secrets_dir)

    def test_safe_cast_failed(self):
        value = get_docker_secret('my_bool_key_true', cast_to=int, safe=True, secrets_dir=self.secrets_dir)
        self.assertIsNone(value)

        with self.assertRaises(ValueError):
            get_docker_secret('my_bool_key_false', cast_to=int, safe=False, secrets_dir=self.secrets_dir)


class TestEnvvar(unittest.TestCase):
    def setUp(self):
        os.environ['MY_KEY'] = 'my_value'
        os.environ['MY_INT_KEY'] = '5'
        os.environ['MY_FLOAT_KEY'] = '5.4'
        os.environ['MY_BOOL_KEY_TRUE'] = 'True'
        os.environ['MY_BOOL_KEY_FALSE'] = 'False'

    def tearDown(self):
        os.environ.pop('MY_KEY')
        os.environ.pop('MY_INT_KEY')
        os.environ.pop('MY_BOOL_KEY_TRUE')
        os.environ.pop('MY_BOOL_KEY_FALSE')

    def test_normal(self):
        value = get_docker_secret('MY_KEY')

        self.assertEqual(value, 'my_value')

    def test_default(self):
        value = get_docker_secret('NOT_EXISTENT')
        self.assertIsNone(value)

        value = get_docker_secret('NOT_EXISTENT', default='a_value')
        self.assertEqual(value, 'a_value')

        value = get_docker_secret('NOT_EXISTENT', default='None')
        self.assertEqual(value, 'None')

    def test_cast(self):
        value = get_docker_secret('MY_INT_KEY', cast_to=int)
        self.assertIsInstance(value, int)
        self.assertEqual(value, 5)

        value = get_docker_secret('MY_FLOAT_KEY', cast_to=float)
        self.assertIsInstance(value, float)
        self.assertEqual(value, 5.4)

        value = get_docker_secret('MY_BOOL_KEY_TRUE', cast_to=bool)
        self.assertIsInstance(value, bool)
        self.assertTrue(value)

        value = get_docker_secret('MY_BOOL_KEY_FALSE', cast_to=bool)
        self.assertIsInstance(value, bool)
        self.assertFalse(value)

    def test_cast_fail(self):
        with self.assertRaises(ValueError):
            get_docker_secret('MY_FLOAT_KEY', cast_to=int, safe=False)

        with self.assertRaises(ValueError):
            get_docker_secret('MY_INT_KEY', cast_to=bool, safe=False)

    def test_autocast_name(self):
        value = get_docker_secret('my_key', autocast_name=True)
        self.assertEqual(value, 'my_value')

        # assumes case-sensitiveness of os. could fail on windows
        value = get_docker_secret('my_key', autocast_name=False)
        self.assertIsNone(value)

    def test_getenv(self):
        value = get_docker_secret('MY_KEY', getenv=True)
        self.assertEqual(value, 'my_value')

        value = get_docker_secret('MY_KEY', getenv=False)
        self.assertIsNone(value)

    def test_safe_not_found(self):
        value = get_docker_secret('INVALID', safe=True)
        self.assertIsNone(value)

        with self.assertRaises(TypeError):
            get_docker_secret('INVALID', safe=False)

    def test_safe_cast_failed(self):
        value = get_docker_secret('MY_BOOL_KEY_TRUE', cast_to=int, safe=True)
        self.assertIsNone(value)

        with self.assertRaises(ValueError):
            get_docker_secret('MY_BOOL_KEY_TRUE', cast_to=int, safe=False)


if __name__ == '__main__':
    unittest.main()
