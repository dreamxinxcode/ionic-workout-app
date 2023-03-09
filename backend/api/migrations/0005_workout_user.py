# Generated by Django 4.1.6 on 2023-03-05 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_remove_workout_use'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='user',
            field=models.OneToOneField(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]