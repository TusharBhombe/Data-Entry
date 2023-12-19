from django.db import models
# from phone_field import PhoneField
# Create your models here.
import uuid

class Customer(models.Model):
    customer_id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    contact = models.CharField(max_length=12, null=True,blank=True)
    customer_number = models.CharField(max_length=20, null=True,blank=True)
    meter_serial_number = models.CharField(max_length=20,null=True,blank=True)

