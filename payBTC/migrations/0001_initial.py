# Generated by Django 4.1 on 2023-02-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Trade",
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
                ("nb", models.CharField(default="0", max_length=20)),
                ("buyer", models.CharField(default="none", max_length=20)),
                ("buy_usd", models.BooleanField(default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
