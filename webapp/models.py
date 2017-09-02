from __future__ import unicode_literals

from django.db import models

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

