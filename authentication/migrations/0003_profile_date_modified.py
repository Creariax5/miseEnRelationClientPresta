# Generated by Django 4.1 on 2023-01-07 07:00

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_profile_delete_students"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="date_modified",
            field=models.DateTimeField(
                auto_now=True, verbose_name=django.contrib.auth.models.User
            ),
        ),
    ]
