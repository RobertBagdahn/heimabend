# Generated by Django 3.0.5 on 2020-04-18 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0020_auto_20200403_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='like_score',
            field=models.IntegerField(default=0),
        ),
    ]
