# Generated by Django 4.0.6 on 2022-07-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0018_mainpage_seo_text_ru_mainpage_seo_text_uk_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='can_delete',
            field=models.BooleanField(default=True),
        ),
    ]
