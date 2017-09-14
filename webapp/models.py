from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class user(models.Model):
    name= models.SlugField(max_length=40,null=True,blank=False)
    age = models.CharField(max_length=50,null=True,blank=True)
    nationality = models.CharField(max_length=100,null=True,blank=False)
    gender = models.CharField(max_length=50,null=True,blank=False)
    address=models.CharField(max_length=1024,null=True,blank=True)
    email=models.CharField(max_length=125,null=True,blank=False)
    fin=models.CharField(max_length=9,null=True,blank=False)
    password=models.CharField(max_length=100,null=False,blank=False,default='test')

class ProductElectronics(models.Model):
    modelName = models.CharField(primary_key=True,max_length=100,null=False,blank=False)
    price = models.IntegerField(null=False,blank=False)
    company=models.CharField(max_length=100,null=False,blank=False)
    iventory = models.IntegerField(null=False,blank=False)
    isActive = models.BooleanField(default=1,null=False,blank=False)
    selledCount = models.IntegerField(null=False,blank=False)
    lastUpdated = models.DateTimeField(default=datetime.now(),null=False,blank=False)


class ProductOrders(models.Model):
    orderId = models.CharField(primary_key=True,max_length=6,null=False,blank=False)
    modelName = models.ForeignKey(ProductElectronics)
    user = models.CharField(max_length=100,null=False,blank=False)
    email = models.CharField(max_length=125,null=False,blank=False)
    quantity = models.IntegerField(null= False,blank=False)
    dateOfPurchase = models.DateTimeField(default=datetime.now(),null=False,blank=False)
    price = models.IntegerField(default=0,null=False,blank=False)