# Generated by Django 4.0.6 on 2022-08-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0046_alter_contacts_date_alter_hall_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsorsale',
            name='describe',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='newsorsale',
            name='describe_ru',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='newsorsale',
            name='describe_uk',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='pages',
            name='describe',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='pages',
            name='describe_ru',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='pages',
            name='describe_uk',
            field=models.TextField(null=True),
        ),
    ]