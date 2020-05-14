from __future__ import unicode_literals

from django.db import models
from phone_field import PhoneField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nazwa kategorii')

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nazwa firmy')
    rating = models.FloatField()
    address = models.CharField(max_length=128, verbose_name='Adres firmy')
    website = models.URLField(max_length=200, verbose_name='Strona internetowa')
    phone = PhoneField(blank=True, help_text='Numer kontaktowy', verbose_name='Numer telefonu')
    category = models.ManyToManyField(Category)
