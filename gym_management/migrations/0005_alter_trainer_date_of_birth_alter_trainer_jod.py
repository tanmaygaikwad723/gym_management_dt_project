# Generated by Django 5.0.6 on 2024-07-07 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gym_management", "0004_alter_trainer_date_of_birth_alter_trainer_jod"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trainer",
            name="date_of_birth",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 7, 7, 19, 12, 39, 754878, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="trainer",
            name="jod",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 7, 7, 19, 12, 39, 754924, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
