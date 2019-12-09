# Generated by Django 3.0 on 2019-12-08 22:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0012_auto_20191205_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='createdByEmail',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(default='', max_length=2000, validators=[django.core.validators.MinLengthValidator(75), django.core.validators.MaxLengthValidator(2000)]),
        ),
    ]