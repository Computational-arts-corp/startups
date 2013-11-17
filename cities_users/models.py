
from django.db import models
from django.utils import timezone

import datetime

class CityBlock(models.Model):
  name = models.CharField(max_length=200, null=True, blank=True, unique=True )
  date = models.DateField( 'moved to on', blank=True, null=True )

  def __unicode__(self):
    return self.name

class Addressbookitem(models.Model):
  name = models.CharField( max_length=200, null=True, blank=True, unique=True )
  descr = models.TextField( null=True, blank=True )

  city_block = models.ForeignKey( CityBlock )

  def __unicode__(self):
    return self.name

class Day(models.Model):
  date = models.CharField(max_length=10)
  a1 = models.CharField(max_length=250)
  a2 = models.CharField(max_length=250)
  a3 = models.CharField(max_length=250)
  a4 = models.CharField(max_length=250)
  a5 = models.CharField(max_length=250)
  dream = models.CharField(max_length=250)
  work = models.CharField(max_length=250)

