from django.core.management.base import BaseCommand, CommandError
from celery_test.tasks import test_task
import time


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(time.time())
        for counter in range(0,100):
            test_task.delay(counter)
        print(time.time())
