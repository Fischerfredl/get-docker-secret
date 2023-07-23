import os

root = os.path.abspath(os.sep)


def get_docker_secret(name, default=None, cast_to=str, autocast_name=True, getenv=True, safe=True,
                      secrets_dir=os.path.join(root, 'run', 'secrets')):
    """This function fetches a docker secret

    :param name: the name of the docker secret
    :param default: the default value if no secret found
    :param cast_to: casts the value to the given type
    :param autocast_name: whether the name should be lowercase for secrets and upper case for environment
    :param getenv: if environment variable should be fetched as fallback
    :param safe: Whether the function should raise exceptions
    :param secrets_dir: the directory where the secrets are stored
    :returns: docker secret or environment variable depending on params
    :raises TypeError: if cast fails due to wrong type (None)
    :raises ValueError: if casts fails due to Value
    """

    # cast name if autocast enabled
    name_secret = name.lower() if autocast_name else name
    name_env = name.upper() if autocast_name else name

    # initiallize value
    value = None

    # try to read from secret file
    try:
        with open(os.path.join(secrets_dir, name_secret), 'r') as secret_file:
            value = secret_file.read().rstrip('\n')
    except IOError as e:
        # try to read from env if enabled
        if getenv:
            value = os.environ.get(name_env)

    # set default value if no value found
    if value is None:
        value = default

    # try to cast
    try:
        # so None wont be cast to 'None'
        if value is None:
            raise TypeError('value is None')

        # special case bool
        if cast_to == bool:
            if value not in ('True', 'true', 'False', 'false'):
                raise ValueError('value %s not of type bool' % value)
            value = 1 if value in ('True', 'true') else 0

        # try to cast
        return cast_to(value)

    except (TypeError, ValueError) as e:
        # whether exception should be thrown
        if safe:
            return default
        raise e
