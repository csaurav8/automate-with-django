# Generated by Django 5.0.2 on 2024-02-12 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='rollno',
            new_name='roll_no',
        ),
    ]
