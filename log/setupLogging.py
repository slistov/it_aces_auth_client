import logging
import logging.config
import yaml
#from asgi_correlation_id.log_filters import correlation_id_filter
from .logConfig import LOGGING_CONFIG

def setupLogging():
    logging.config.dictConfig(LOGGING_CONFIG)
