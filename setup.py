from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='get-docker-secret',
    version='2.0.0',
    description='Utility function to fetch docker secrets/envvars.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/fischerfredl/get-docker-secret',
    author='Alfred Melch',
    author_email='dev@melch.pro',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    keywords=['docker', 'secret', 'envvar', 'config'],
    py_modules=['get_docker_secret'],
    install_requires=[],
    test_suite='tests',
    tests_require=[],
)
