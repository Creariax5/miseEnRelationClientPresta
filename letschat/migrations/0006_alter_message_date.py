# Generated by Django 4.1 on 2023-01-25 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("letschat", "0005_message_last_alter_message_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="date",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 1, 25, 19, 42, 13, 590993)
            ),
        ),
    ]
