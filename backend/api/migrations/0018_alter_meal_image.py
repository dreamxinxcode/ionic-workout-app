# Generated by Django 4.1.6 on 2023-06-12 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_meal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.ImageField(default='default.png', upload_to='meals/<function generate_unique_filename at 0x7fc53987bca0>'),
        ),
    ]