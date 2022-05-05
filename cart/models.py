from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
class Order(models.Model):
    City_choise = [
        ('L', 'Lviv'),
        ('S', 'Striy'),
    ]
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(blank=True, null=True,  verbose_name="Mail")
    phone = PhoneNumberField(unique = True, null = False, blank = False,  verbose_name="Phone number")
    city = models.CharField(choices=City_choise, max_length=1,  verbose_name="City")
    street = models.CharField(max_length=100,  verbose_name="Street")
    street_number = models.PositiveIntegerField(verbose_name="Street number")
