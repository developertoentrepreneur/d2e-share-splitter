# Generated by Django 3.2.9 on 2022-01-07 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sharecontributions", "0005_rename_value_contribution_amount"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contribution",
            old_name="projectType",
            new_name="project",
        ),
    ]
