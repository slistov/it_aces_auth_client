import os
import yaml
config = yaml.safe_load(open("config.yaml", mode="r", encoding="utf-8"))

#DATABASE_URL = os.getenv('DB_URI')

# oauth2 API
OAUTH_CONF = config['OAUTH']

# LOGGING
ERROR_LOG_FILENAME = config['ERROR_LOG_FILENAME']

