# Generated by Django 4.1 on 2023-01-31 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0008_remove_product_my_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="display",
            field=models.BooleanField(default=False),
        ),
    ]