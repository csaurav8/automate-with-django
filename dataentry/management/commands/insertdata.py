from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = "This will insert data to the database"

    def handle(self, *args, **kwargs):
        dataset = [
            {'roll_no':'12011', 'name':"saurav", 'age':28},
            {'roll_no':'12012', 'name':"riya", 'age':25},
            {'roll_no':'12013', 'name':"rohit", 'age':30},
        ]

        for data in dataset:
            roll_no = data['rollno']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()

            if not existing_record:
                Student.objects.create(rollno=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Data with {roll_no} already exists'))

        self.stdout.write(self.style.SUCCESS('Data Inserted Successfully!'))