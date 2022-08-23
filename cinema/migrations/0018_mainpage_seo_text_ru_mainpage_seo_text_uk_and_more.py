# Generated by Django 4.0.6 on 2022-07-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0017_contacts_date_mainpage_date_pages_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='seo_text_ru',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='seo_text_uk',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='title_ru',
            field=models.CharField(default='Главная страница', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='title_uk',
            field=models.CharField(default='Главная страница', max_length=40, null=True),
        ),
    ]
