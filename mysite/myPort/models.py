# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Airports(models.Model):
    code = models.CharField(blank=True, null=True,max_length=5)
    lat = models.CharField(blank=True, null=True, max_length=10)
    lon = models.CharField(blank=True, null=True, max_length=10)
    name = models.CharField(blank=True, null=True, max_length=50)
    rating = models.FloatField()
    city = models.CharField(blank=True, null=True, max_length=50)
    state = models.CharField(blank=True, null=True, max_length=50)
    country = models.CharField(blank=True, null=True, max_length=50)
    tz = models.CharField(blank=True, null=True, max_length=50)
    type = models.CharField(blank=True, null=True, max_length=50)
    url = models.CharField(blank=True, null=True, max_length=200)
    elev = models.CharField(blank=True, null=True, max_length=20)
    direct_flights = models.CharField(blank=True, null=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'mmt'
