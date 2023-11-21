import time
from celery.result import AsyncResult
from django.core.management import BaseCommand
from celery_test.tasks import send_sms

class Command(BaseCommand):
    def handle(self, *args, **options):
        number = '0912*********'
        message = 'learning is fun'
        result = send_sms.delay(number, message)
        print(result)
        print(result.id)
