# Generated by Django 3.0 on 2020-01-22 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0015_auto_20200119_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
