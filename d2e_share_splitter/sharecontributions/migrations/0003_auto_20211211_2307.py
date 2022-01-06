# Generated by Django 3.2.9 on 2021-12-11 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharecontributions', '0002_remove_contribution_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='value',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='hours',
            field=models.FloatField(blank=True, null=True),
        ),
    ]