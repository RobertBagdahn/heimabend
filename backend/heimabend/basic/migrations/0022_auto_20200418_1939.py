# Generated by Django 3.0.5 on 2020-04-18 19:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0021_event_like_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(default='', max_length=5500, validators=[django.core.validators.MinLengthValidator(75), django.core.validators.MaxLengthValidator(5500)]),
        ),
        migrations.AlterField(
            model_name='event',
            name='material',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
