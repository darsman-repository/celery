import random
from celery import shared_task
from celery.contrib import rdb
import time


@shared_task
def test_task():
    time.sleep(1)
    print(f"hello world")


@shared_task
def send_sms(mobile, message):
    print(mobile)
    print(message)
    time.sleep(3)
    rnd = random.randint(0,10)
    if rnd % 2 == 0:
        return True
    return False

@shared_task
def debugging():
    rnd = random.randint(0, 10)
    name = __name__
    mobile = '09128*******'
    rdb.set_trace()
    return rnd
