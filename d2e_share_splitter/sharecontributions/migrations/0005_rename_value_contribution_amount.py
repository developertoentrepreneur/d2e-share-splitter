# Generated by Django 3.2.9 on 2022-01-07 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sharecontributions", "0004_auto_20211212_1932"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contribution",
            old_name="value",
            new_name="amount",
        ),
    ]
