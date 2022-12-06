from django.db import models

# Create your models here.
class ClientBooking(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120,default='')
    checkin = models.DateField()
    checkout = models.DateField()

class MpesaResponse(models.Model):
    msg = models.CharField(max_length=5000,null=True,blank=True)