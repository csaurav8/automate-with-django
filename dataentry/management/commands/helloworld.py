from django.core.management import BaseCommand

class Command(BaseCommand):
    help = "Prints Hello World"

    def handle(self, *args, **kwargs):
        self.stdout.write("Hello World")