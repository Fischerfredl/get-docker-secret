from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='get-docker-secret',
    version='1.0.0',
    description='Utility function to fetch docker secrets/envvars.',
    long_description=readme(),
    url='https://github.com/fischerfredl/get-docker-secret',
    author='Alfred Melch',
    author_email='alfred.melch@gmx.de',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=['docker', 'secret', 'envvar', 'config'],
    py_modules=['get_docker_secret'],
    install_requires=[],
    test_suite='tests',
    tests_require=[],
)
