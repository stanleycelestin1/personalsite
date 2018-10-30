import datetime

from django.db import models
from django.utils import timezone

# Create your models here.



class Contact(models.Model):
    first_name = models.CharField(max_length=25)
    last_name  = models.CharField(max_length=25)
    email_address = models.CharField(max_length=50)

    date_contacted = models.DateTimeField('date contacted')

