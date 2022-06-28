# from asgi_correlation_id.log_filters import correlation_id_filter
import logging
from app.core.config import ERROR_LOG_FILENAME

class infoFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.INFO


class debugFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.DEBUG


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        #'correlation_id': {'()': correlation_id_filter(uuid_length=32)},
        'debugFilter': {'()': debugFilter},
        'infoFilter': {'()': infoFilter},
    },
    'formatters': {
        'web_info': {
            'class': 'logging.Formatter',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'format': '%(asctime)s %(levelname)s ID: [%(correlation_id)s] %(name)s %(message)s',
        },
        'web_debug': {
            'class': 'logging.Formatter',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'format': '%(asctime)s.%(msecs)03d'+
                ' %(levelname)s' +
                # ' ID: [%(correlation_id)s]' +
                ' %(name)s %(message)s'
        },
        "default": {
            # "format": "%(asctime)s.%(msecs)03d:%(name)s:%(process)d:%(lineno)d " "%(levelname)s %(message)s",  
            "format": "%(asctime)s.%(msecs)03d " "%(levelname)s %(message)s",  
            # "datefmt": "%Y-%m-%d %H:%M:%S",  
            "datefmt": "%H:%M:%S",  
        },
        "simple": {  
            "format": "%(message)s",  
        },
    },
    'handlers': {
        'logfile': {
            'formatter': 'default',
            # 'class': 'logging.StreamHandler',
            # 'stream': 'ext://sys.stdout',
            'level': 'DEBUG', # All
            # 'level': 'ERROR', # Error and Critical
            "class": "logging.handlers.RotatingFileHandler",
            "filename": ERROR_LOG_FILENAME, 
            "backupCount": 2, 
            # 'filters': ['correlation_id', 'debugFilter'],
        },
        "verbose_output": {  
            # "formatter": "simple",  
            "formatter": "default",  
            "level": "DEBUG",  # All
            "class": "logging.StreamHandler",  
            "stream": "ext://sys.stdout", 
        },
    },
    'loggers': {
        'app.main': {
            'handlers': [
                'logfile', 
                'verbose_output'
            ],
            'level': 'DEBUG',
            # 'propagate': True,
        },
    },
    'root': {
        "level": "INFO",  
        "handlers": [
            # "logfile",  
        ]
    }
}