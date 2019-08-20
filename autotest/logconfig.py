import os
from celery import Celery
from kombu import Exchange, Queue
import logging
from logging.handlers import TimedRotatingFileHandler


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# celery
app = Celery('demo', broker='amqp://guest@localhost:5672//')
# Queue
queue = (
    # 定义专用的queue,定义Exchange,以及与route对应的key
    Queue('queue_demo', Exchange('exchange_demo', type='direct'),
    routing_key='queue_demo_key'),
)
# Route
route = {
    # 定义任务crontab_func1的queue,routing_key
    'tasks.crontab_func1': {'queue': 'queue_demo', 'routing_key': 'queue_demo_key'},
    'tasks.crontab_func2': {'queue': 'queue_demo', 'routing_key': 'queue_demo_key'},
}

# 指定queue和route的配置应用到celery定时任务的配置中,设置时区
app.conf.update(CELERY_QUEUES=queue, CELERY_ROUTES=route, CELERY_TIMEZONE='Asia/Shanghai', CELERY_ENABLE_UTC=False)


class Config(object):

    # 设置日志
    log_fmt = '%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s'

    # log_file_handler = TimedRotatingFileHandler(filename="log", when="MIDNIGHT", interval=1, backupCount=30)
    log_file_handler = TimedRotatingFileHandler(filename=os.path.join(BASE_DIR, 'logs/apitest.log'), when="M", interval=1, backupCount=7)
    formatter = logging.Formatter(log_fmt)
    log_file_handler.setFormatter(formatter)

    logging.basicConfig(format=log_fmt)
    LOGGER = logging.getLogger()
    LOGGER.setLevel(logging.INFO)

    LOGGER.addHandler(log_file_handler)


