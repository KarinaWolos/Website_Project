from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Kategoria')

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nazwa firmy')
    rating = models.DecimalField(default=5, decimal_places=1, max_digits=3, validators=[MinValueValidator(0), MaxValueValidator(5)])
    address = models.CharField(max_length=128, verbose_name='Adres firmy')
    website = models.URLField(max_length=200, verbose_name='Strona internetowa')
    phone = PhoneNumberField(blank=True, verbose_name='Numer telefonu')
    category = models.ManyToManyField(Category, verbose_name='Kategoria')
