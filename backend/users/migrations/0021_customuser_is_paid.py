# Generated by Django 4.1.6 on 2023-05-01 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_customuser_pr'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]