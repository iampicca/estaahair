# Generated by Django 2.0.7 on 2018-08-17 23:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('estaaweb', '0008_auto_20180805_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 17, 23, 6, 23, 402166, tzinfo=utc)),
        ),
    ]
