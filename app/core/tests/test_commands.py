from unittest.mock import patch
from django.core.management import call_command
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):

    def wait_for_db_mock_ready(self,patched_check):
        """Mock for the Command.check method to simulate database availability."""
        print('>>>>>')
        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(databases=['default'])
