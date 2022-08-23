# Generated by Django 4.0.6 on 2022-07-15 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0006_remove_hall_number_hall_date_hall_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='title',
        ),
        migrations.AlterField(
            model_name='hall',
            name='date',
            field=models.DateField(default=datetime.date(2022, 7, 15)),
        ),
    ]
