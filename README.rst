|version| |license| |pyversions| |pipeline status| |coverage|

get-docker-secret
=================

Utility function to fetch docker secrets/envvars.

For config values (flask projects) i like to fetch docker secrets and
fall back to environment variables for development. This module provides
a function to make this a one-liner: use docker secret -> fall back to
envvar -> fall back to default value.

The function also provides the possibility to automatically cast the
value or specify a custom directory for secrets.

Following assumptions are being made (params): \*
``autocast_name=True``: secrets are lower-case, envvars upper-case.
automatic conversion of name can be switched off via
autocast\_name=False \* ``cast_to=str``: fill in desired datatype.
special case bool: 'True'/'true' will be True. 'False'/'false' will be
False \* ``envvar=True``: you want to fall back to envvar. can be
switched of via envvar=False \* ``default=None`` \* ``safe=True``:
returns None if name not found or cast fails. If you want exceptions:
safe=False \* ``secrets_dir=/var/run/secrets``

Usage
-----

.. code:: python

    from get_docker_secret import get_docker_secret

    value = get_docker_secret('secret_key', default='very_secret')

Testing
-------

.. code:: python

    python setup.py test

not tested under windows

.. |version| image:: https://img.shields.io/pypi/v/get-docker-secret.svg
   :target: https://pypi.python.org/pypi/get-docker-secret
.. |license| image:: https://img.shields.io/pypi/l/get-docker-secret.svg
   :target: https://pypi.python.org/pypi/get-docker-secret
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/get-docker-secret.svg
   :target: https://pypi.python.org/pypi/get-docker-secret
.. |pipeline status| image:: https://travis-ci.org/Fischerfredl/get-docker-secret.svg?branch=master
   :target: https://travis-ci.org/Fischerfredl/get-docker-secret
.. |coverage| image:: https://img.shields.io/codecov/c/github/fischerfredl/get-docker-secret.svg
   :target: https://codecov.io/gh/Fischerfredl/get-docker-secret
