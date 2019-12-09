# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator


class Tag(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    title = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(5),
            MaxLengthValidator(40)])
    description = models.CharField(
        max_length=2000,
        default='',
        validators=[
            MinLengthValidator(75),
            MaxLengthValidator(2000)])
    isPossibleOutside = models.BooleanField(default=1)
    isPossibleInside = models.BooleanField(default=1)
    tags = models.ManyToManyField(Tag, default='')
    material = models.CharField(max_length=200, default='')
    costsRating = models.SmallIntegerField(
        default=1, validators=[
            MinValueValidator(1), MaxValueValidator(3)])
    executionTimeRating = models.SmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(3)])
    isPrepairationNeeded = models.BooleanField(default=1)
    isActive = models.BooleanField(default=0)
    isLvlOne = models.BooleanField(default=1)
    isLvlTwo = models.BooleanField(default=0)
    isLvlThree = models.BooleanField(default=0)
    createdBy = models.CharField(max_length=60, default='')
    createdByEmail = models.CharField(max_length=60, default='')
    updatedBy = models.CharField(max_length=60, null=True, blank=True)
    createdAt = models.DateTimeField(default=now, editable=False)
    updatedAt = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
