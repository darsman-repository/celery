from celery import shared_task
import time

@shared_task
def test_task(counter: int):
    time.sleep(10)
    print(f"{counter} - LEARNING IS FUN :D ")