# Generated by Django 3.1.4 on 2020-12-12 15:43

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0005_auto_20201211_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
