from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as psycopg2error
from django.db.utils import OperationalError
import time
#django command to wait for postgres to be available
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("waiting for DB")
        db_up = False
        while db_up is False:
            try:
                self.check(databases = ['default'])
                db_up=True
            except (psycopg2error,OperationalError):
                self.stdout.write('DB unavailable waiting for 1 sec')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('DB connected successfully'))
        