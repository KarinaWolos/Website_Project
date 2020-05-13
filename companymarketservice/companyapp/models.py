from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nazwa kategorii')

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nazwa firmy')
    rating = models.DecimalField(decimal_places=1, verbose_name='Ocena')
    address = models.CharField(max_length=128, verbose_name='Adres firmy')
    website = models.URLField(max_length=200, verbose_name='Strona internetowa')
    phone = models.CharField(max_length=12, verbose_name='Numer telefonu')
