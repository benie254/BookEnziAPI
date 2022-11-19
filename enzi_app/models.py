from django.db import models

# Create your models here.
class ClientBooking(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120,default='')
    checkin_date = models.DateField()
    checkout_date = models.DateField()