# Generated by Django 4.0.6 on 2022-08-01 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0044_alter_bannerbox_turning_speed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerbox',
            name='turning_speed',
            field=models.CharField(choices=[('3', '3'), ('5', '5'), ('10', '10')], default='3', max_length=32),
        ),
    ]