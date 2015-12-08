import sys

from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.migrations.autodetector import MigrationAutodetector
from django.db.migrations.executor import MigrationExecutor
from django.db.migrations.state import ProjectState
from django.db.utils import OperationalError


class Command(BaseCommand):
    """
    Detect if any apps have missing migration files

    (not necessaily applied though)
    """
    help = "Detect if any apps have missing migration files"

    def handle(self, *args, **kwargs):

        changed = set()
        ignore_list = ['authtools']  # dependencies that we don't care about migrations for (usually for testing only)

        self.stdout.write("Checking...")
        for db in settings.DATABASES.keys():

            try:
                executor = MigrationExecutor(connections[db])
            except OperationalError:
                sys.exit("Unable to check migrations: cannot connect to database\n")

            autodetector = MigrationAutodetector(
                executor.loader.project_state(),
                ProjectState.from_apps(apps),
            )

            changed.update(autodetector.changes(graph=executor.loader.graph).keys())

        for ignore in ignore_list:
            if ignore in changed:
                changed.remove(ignore)

        if changed:
            sys.exit("Apps with model changes but no corresponding migration file: %(changed)s\n" % {
                'changed': list(changed)
            })
        else:
            sys.stdout.write("All migration files present\n")
