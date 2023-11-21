from django.core.management import BaseCommand
from celery_test.tasks import debugging

class Command(BaseCommand):
    def handle(self, *args, **options):
        debugging.delay()