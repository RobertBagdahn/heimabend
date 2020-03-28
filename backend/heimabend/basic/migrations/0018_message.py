# Generated by Django 3.0 on 2020-03-27 16:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0017_auto_20200322_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('topic', models.CharField(max_length=40)),
                ('messageBody', models.CharField(max_length=1000)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]