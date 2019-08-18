from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms
from celery.schedules import crontab
from datetime import timedelta

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autotest.settings')

app = Celery('autotest')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# 允许root 用户运行celery
platforms.C_FORCE_ROOT = True

# celery每个 worker 执行 10 个任务后kill 掉
CELERYD_MAX_TASKS_PER_CHILD = 10

# redis做MQ配置
#app = Celery('website', backend='redis', broker='redis://localhost')
# rabbitmq做MQ配置
app = Celery('autotest', backend='amqp', broker='amqp://guest@localhost')


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.update(
    CELERYBEAT_SCHEDULE={
        #        'async-task': {
        #        'task': 'apitest.tasks.getSum',
        #        'schedule': timedelta(seconds=20),
        #        'args': (4)
        #        }
        'sum-task': {
            'task': 'apitest.tasks.getSum',
            'schedule': timedelta(minutes=1),
            'args': (4,)
        }
    }
)
