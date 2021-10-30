import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution untile the db is available."""

    def handle(self, *args, **kwargs):
        self.stdout.write('waiting for databases.')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Db unavailable, please wait 1 sec')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))
