# Generated by Django 4.0.6 on 2022-07-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0031_alter_backgroundbanner_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerbox',
            name='status',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
