# Generated by Django 4.0.6 on 2022-07-15 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0007_remove_photo_title_alter_hall_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='pictures',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema.gallery', verbose_name='Галерея картинок'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='seo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema.seo', verbose_name='СЕО блок'),
        ),
    ]
