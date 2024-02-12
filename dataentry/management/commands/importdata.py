from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv

from dataentry.models import Student

class Command(BaseCommand):
    help = "Imports data from csv"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="sets the path of csv")
        parser.add_argument("model_name", type=str, help="sets the path of csv")


    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        model_name = kwargs["model_name"]

        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue

        if not model:
            raise CommandError(f'Model "{model_name}" not found in any apps!')

        with open(file_path, 'r' ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Data imported from csv successfully!'))
