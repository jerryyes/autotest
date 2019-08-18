import logging.config

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            # 'datefmt': '%m-%d-%Y %H:%M:%S'
            'format': '%(asctime)s \"%(pathname)s：%(module)s:%(funcName)s:%(lineno)d\" [%(levelname)s]- %(message)s'
        }
    },
    'handlers': {
        'celery': {
            # 'level': 'INFO',
            # 'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '/Users/chenzhiyuan/PycharmProjects/autotest/logs/apitest.log',
            'when': 'midnight',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
         'apitest': {
            'handlers': ['celery'],
            'level': 'INFO',
            'propagate': True,
         }
    }
}

logging.config.dictConfig(LOG_CONFIG)

