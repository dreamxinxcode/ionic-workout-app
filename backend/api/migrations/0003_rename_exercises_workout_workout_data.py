# Generated by Django 4.1.6 on 2023-02-05 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_workout_exercises_workout_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workout',
            old_name='exercises',
            new_name='workout_data',
        ),
    ]
