[![version](https://img.shields.io/pypi/v/get-docker-secret.svg)](https://pypi.python.org/pypi/get-docker-secret)
[![license](https://img.shields.io/pypi/l/get-docker-secret.svg)](https://pypi.python.org/pypi/get-docker-secret)
[![pyversions](https://img.shields.io/pypi/pyversions/get-docker-secret.svg)](https://pypi.python.org/pypi/get-docker-secret)
[![coverage](https://img.shields.io/codecov/c/github/fischerfredl/get-docker-secret.svg)](https://codecov.io/gh/Fischerfredl/get-docker-secret)

# get-docker-secret

Utility function to fetch docker secrets/envvars.

For config values (flask projects) i like to fetch docker secrets and fall back to environment variables for development. This module provides a function to make this a one-liner: use docker secret -> fall back to envvar -> fall back to default value.

The function also provides the possibility to automatically cast the value or specify a custom directory for secrets.

Following assumptions are being made (params):

- `autocast_name=True`: secrets are lower-case, envvars upper-case. automatic conversion of name can be switched off via autocast_name=False
- `cast_to=str`: fill in desired datatype. special case bool: 'True'/'true' will be True. 'False'/'false' will be False
- `getenv=True`: you want to fall back to envvar. can be switched of via getenv=False
- `default=None`
- `safe=True`: returns None if name not found or cast fails. If you want exceptions: safe=False
- `secrets_dir=/var/run/secrets`

## Usage

```python
from get_docker_secret import get_docker_secret

value = get_docker_secret('secret_key', default='very_secret')
```

## Testing

```python
python setup.py test
```

not tested under windows

## Changelog


### 2.0.0 - 2023-07-23

- Changed: Use canonical `/run/secrets` directory to read secrets from (changed from `/var/run/secrets`) (PR #4) (Thanks @ThorpeJosh)

### 1.0.2 - 2021-03-19

- Fixed: Only strip trailing newlines from secrets file

### 1.0.1 - 2019-12-07

- Fixed: Strip values read from file.

### 1.0.0 - 2018-01-30

- Initial publish
