from django.core.management.base import BaseCommand, CommandError
from celery_test.tasks import test_task
import time, logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        for counter in range(0,100):
            print(f"start - {time.time()}")
            test_task.delay(counter)
            print(f"end - {time.time()}")
