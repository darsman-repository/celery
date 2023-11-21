from django.core.management import BaseCommand
from celery.result import AsyncResult

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--id', type=str)

    def handle(self, *args, **options):
        id = options['id']
        response= AsyncResult(id)
        print(response.result)