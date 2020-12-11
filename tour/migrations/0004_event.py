# Generated by Django 3.1.4 on 2020-12-11 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_auto_20201211_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('event_description', models.TextField()),
                ('event_img_1', models.ImageField(default='', upload_to='events')),
                ('event_img_2', models.ImageField(default='', upload_to='events')),
                ('event_img_3', models.ImageField(default='', upload_to='events')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('event_location', models.CharField(max_length=500)),
                ('event_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tour.category')),
            ],
        ),
    ]
