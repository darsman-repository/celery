import random

from celery import shared_task
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