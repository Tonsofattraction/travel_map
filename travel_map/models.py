'''
Created on Aug 11, 2014

@author: noob
'''

from django.db import models

class Country(models.Model):
    n = models.AutoField(primary_key=True)
    name = models.CharField(max_length=8)
    code = models.CharField(max_length=64)
    value = models.BooleanField(default=False)
    