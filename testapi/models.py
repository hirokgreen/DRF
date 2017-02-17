"""models classs for testapi app"""
from __future__ import unicode_literals
from django.db import models

class Contact(models.Model):
    """contact table with name,email and address, name will be the row title"""
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    address = models.CharField(max_length=400)
    def __str__(self):
        return self.name
