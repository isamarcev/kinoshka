# Generated by Django 4.0.6 on 2022-08-16 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0064_alter_contacts_date_alter_hall_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
