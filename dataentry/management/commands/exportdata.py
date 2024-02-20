from django.core.management.base import BaseCommand
from django.apps import apps
import csv
import datetime

# proposed command = python manage.py exportdata model_name
class Command(BaseCommand):
    help="Export data from database to a csv file"

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help="Model Name")

    def handle(self, *args, **kwargs):
        model_name=kwargs['model_name'].capitalize()

        # search through all the installed apps for model_name
        model = None

        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                pass

        if not model:
            self.stderr.write(self.style.WARNING(f'model {model_name} not found!'))
            return

        # fetch the data from db
        data = model.objects.all()
        
        # timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

        # define path for csv file
        file_path = f'export_{model_name}_data_{timestamp}.csv'

        # open csv file and print the field names of the model that we are trying to export
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
        
            # Write the csv header
            writer.writerow([field.name for field in model._meta.fields])

            # Write the rows of model
            for item in data:
                writer.writerow([getattr(item, field.name) for field in model._meta.fields])
        
        self.stdout.write(self.style.SUCCESS(self.style.SUCCESS(f'Data Exported to {file_path} successfully!')))

