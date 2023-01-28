# Generated by Django 4.1 on 2023-01-25 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("letschat", "0004_alter_message_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="last",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="message",
            name="date",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 1, 25, 19, 18, 5, 459208)
            ),
        ),
    ]
