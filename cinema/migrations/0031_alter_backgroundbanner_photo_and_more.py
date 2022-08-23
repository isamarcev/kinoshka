# Generated by Django 4.0.6 on 2022-07-25 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0030_bannerbox_news_or_main_alter_bannerbox_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundbanner',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='backgroundbanner/', verbose_name='Фото на фоне'),
        ),
        migrations.AlterField(
            model_name='backgroundbanner',
            name='type',
            field=models.CharField(blank=True, choices=[('Фото на фоне', 'фото на фоне'), ('Пустой фон', 'Пустой фон')], max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='Название кинотеатра'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='name_ru',
            field=models.CharField(max_length=32, null=True, unique=True, verbose_name='Название кинотеатра'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='name_uk',
            field=models.CharField(max_length=32, null=True, unique=True, verbose_name='Название кинотеатра'),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='Название фильма'),
        ),
        migrations.AlterField(
            model_name='film',
            name='title_ru',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='Название фильма'),
        ),
        migrations.AlterField(
            model_name='film',
            name='title_uk',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='Название фильма'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='title',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='Заголовок СЕО'),
        ),
    ]
