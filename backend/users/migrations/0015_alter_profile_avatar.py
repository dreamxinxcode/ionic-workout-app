# Generated by Django 4.1.6 on 2023-04-27 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_profile_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='/media/avatar.jpg', null=True, upload_to='avatars'),
        ),
    ]