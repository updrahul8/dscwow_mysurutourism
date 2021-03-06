# Generated by Django 3.1.4 on 2020-12-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0006_place_geolocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='geolocation',
        ),
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
