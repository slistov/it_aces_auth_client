import os
import yaml
config = yaml.safe_load(open("config.yaml", mode="r", encoding="utf-8"))

#DATABASE_URL = os.getenv('DB_URI')

GET_USER_TOKEN = config['GET_USER_TOKEN']
AUTHORIZATIONS = config['AUTHORIZATIONS']

# oauth2 API
_OAUTH_CONF = config['OAUTH']
_URL = _OAUTH_CONF['URL']
_API = _OAUTH_CONF['API']
OAUTH_LOGIN = f"{_URL}{_API['LOGIN']}"
OAUTH_AUTHORIZE = f"{_URL}{_API['AUTHORIZE']}"
OAUTH_TOKEN = f"{_URL}{_API['TOKEN']}"
OAUTH_TOKEN_INFO = f"{_URL}{_API['TOKEN_INFO']}"
OAUTH_USER_INFO = f"{_URL}{_API['USER_INFO']}"

# LOGGING
ERROR_LOG_FILENAME = config['ERROR_LOG_FILENAME']

