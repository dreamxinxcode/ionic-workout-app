# Generated by Django 4.1.6 on 2023-04-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_profile_units_profile_units_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='units_height',
            field=models.CharField(choices=[('metric', 'Metric'), ('imperial', 'Imperial')], default='imperial', max_length=8),
        ),
        migrations.AlterField(
            model_name='profile',
            name='units_weight',
            field=models.CharField(choices=[('metric', 'Metric'), ('imperial', 'Imperial')], default='imperial', max_length=8),
        ),
    ]
