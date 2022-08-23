# Generated by Django 4.0.6 on 2022-07-12 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_pages_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='IMAX',
            field=models.BooleanField(default=False, null=True, verbose_name='IMAX'),
        ),
        migrations.AlterField(
            model_name='film',
            name='date_of_premier',
            field=models.DateTimeField(null=True, verbose_name='Дата премьеры'),
        ),
        migrations.AlterField(
            model_name='film',
            name='f2d',
            field=models.BooleanField(default=False, null=True, verbose_name='2D'),
        ),
        migrations.AlterField(
            model_name='film',
            name='f3d',
            field=models.BooleanField(default=False, null=True, verbose_name='3D'),
        ),
        migrations.AlterField(
            model_name='film',
            name='logo',
            field=models.ImageField(null=True, upload_to='film/', verbose_name='Логотип фильма'),
        ),
        migrations.AlterField(
            model_name='film',
            name='pictures',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema.gallery', verbose_name='Картинки'),
        ),
        migrations.AlterField(
            model_name='film',
            name='seo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='cinema.seo', verbose_name='SEO блок'),
        ),
    ]
