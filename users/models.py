from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    address = models.CharField(max_length=100, verbose_name='Адресс', null=True, blank=True)
    number_of_card = models.BigIntegerField(verbose_name="Номер карты банка", null=True, blank=True)
    language = models.CharField(max_length=25, choices=[('r', 'Russian'), ('u', 'UA')], null=True, blank=True)
    sex = models.CharField(max_length=24, choices=[('m', 'male'), ('f', 'female')], null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
