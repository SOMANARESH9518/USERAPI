from django.db import models
# from django.utils import timezone
from django.core.validators import RegexValidator
from .choices import *


class APIUser(models.Model):
    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(choices=STATE_CHOICE, max_length=50, null=True)
    city_or_town = models.CharField(max_length=60, default='')
    email = models.EmailField(max_length=60, unique=True, blank=False, null=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format:\
                                  L̥'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)  # validators should be a list
    gender = models.CharField(choices=GENDER, max_length=10, default='M')
