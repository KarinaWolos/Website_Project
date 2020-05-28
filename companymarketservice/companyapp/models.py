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
    rating = models.DecimalField(default=5, decimal_places=1, max_digits=3,
                                 validators=[MinValueValidator(0), MaxValueValidator(5)])
    street = models.CharField(max_length=128, verbose_name='Ulica i numer mieszkania')
    city = models.CharField(max_length=128, verbose_name='Miasto')
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)
    website = models.URLField(max_length=200, verbose_name='Strona internetowa')
    phone = PhoneNumberField(blank=True, verbose_name='Numer telefonu')
    category = models.ManyToManyField(Category, verbose_name='Kategoria')

    @property
    def x_value(self):
        return "{}".format(self.x)

    @property
    def y_value(self):
        return "{}".format(self.y)
