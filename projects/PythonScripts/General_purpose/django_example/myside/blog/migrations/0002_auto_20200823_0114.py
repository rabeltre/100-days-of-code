# Generated by Django 3.0.8 on 2020-08-23 05:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 23, 5, 14, 9, 216631, tzinfo=utc)),
        ),
    ]
