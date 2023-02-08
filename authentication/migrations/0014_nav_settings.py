# Generated by Django 4.1 on 2023-02-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0013_profile_my_pokemons_alter_profile_my_objects"),
    ]

    operations = [
        migrations.CreateModel(
            name="nav_settings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="none", max_length=40)),
                ("bool", models.BooleanField(default=False)),
            ],
        ),
    ]