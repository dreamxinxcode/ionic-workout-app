# Generated by Django 4.1.6 on 2023-05-06 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0011_exercisefavorites'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercisefavorites',
            options={'verbose_name_plural': 'Exercise Favorites'},
        ),
        migrations.RemoveField(
            model_name='workout',
            name='workout_data',
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.workout')),
            ],
        ),
    ]