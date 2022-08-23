# Generated by Django 4.0.6 on 2022-07-15 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0008_alter_cinema_pictures_alter_cinema_seo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='pictures',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema.gallery', verbose_name='Галерея картинок'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='seo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema.seo', verbose_name='СЕО блок'),
        ),
    ]