from __future__ import absolute_import
from celery import shared_task
from celery.utils.log import get_task_logger
from autotest import logconfig

logger = get_task_logger('apitest')
@shared_task
def getSum(n):
    rangelist = []
    sum = 0
    for i in range(1, n):
        sum += i
        rangelist.append(str(i))
    SumExp = '+'.join(rangelist)
    print("%s = %s" % (SumExp, sum))
    logger.info("%s = %s" % (SumExp, sum))
    return SumExp, sum
