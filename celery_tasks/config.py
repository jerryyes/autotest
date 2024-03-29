from celery.schedules import crontab
import logging.config
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 指定任务队列的位置
# rabbitMQ
# BROKER_URL = "amqp://guest@localhost:5672//"
# redis
BROKER_URL = "redis://127.0.0.1/0"
# 指定消息执行结果的位置
# rabbitMQ
#CELERY_RESULT_BACKEND = "amqp://guest@localhost:5672//"
# redis
CELERY_RESULT_BACKEND = "redis://127.0.0.1/0"
# 一定要写下面这句，指定时区，否则celery默认使用utc时间，设置的hour会延迟8小时执行
CELERY_TIMEZONE = 'Asia/Shanghai'

# 这里列出了三个最典型的定时任务，更多用法自行百度crontab语法
CELERYBEAT_SCHEDULE = {
    # 定时任务一：　每5分钟执行一次任务(getSum)
    'getSum': {
        "task": "celery_tasks.apitest.tasks.getSum",
        "schedule": crontab(hour='*/5'),
        "args": (4,),
    },
}

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s \"%(pathname)s：%(module)s:%(funcName)s:%(lineno)d\" [%(levelname)s]- %(message)s'
        }
    },
    'handlers': {
        'celery': {
            'level': 'INFO',
            'formatter': 'simple',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/celery.log'),
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'celery': {
            'handlers': ['celery'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

logging.config.dictConfig(LOG_CONFIG)
