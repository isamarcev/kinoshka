# Generated by Django 4.0.6 on 2022-08-14 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0060_alter_ticket_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='date',
            field=models.DateField(default=datetime.date(2022, 8, 14)),
        ),
        migrations.AlterField(
            model_name='hall',
            name='date',
            field=models.DateField(default=datetime.date(2022, 8, 14)),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='date',
            field=models.DateField(default=datetime.date(2022, 8, 14)),
        ),
        migrations.AlterField(
            model_name='pages',
            name='date',
            field=models.DateField(default=datetime.date(2022, 8, 14)),
        ),
    ]
