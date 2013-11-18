
from django.db import models
from django.utils import timezone

import datetime

class City(models.Model):
  name = models.CharField(max_length=200)

  def __unicode__(self):
    return self.name

class CityBlock(models.Model):
  name = models.CharField(max_length=200, null=True, blank=True, unique=True )
  date = models.DateField( 'moved to on', blank=True, null=True )
 
  # city = models.ForeignKey(City, null=True)

  def __unicode__(self):
    return self.name

class Addressbookitem(models.Model):
  name = models.CharField( max_length=200, null=True, blank=True, unique=True )
  descr = models.TextField( null=True, blank=True )

  city_block = models.ForeignKey( CityBlock )
  city = models.ForeignKey( City, blank=True,null=True )

  def __unicode__(self):
    return self.name

class Day(models.Model):
  date = models.CharField(max_length=10, unique=True)
  a1 = models.CharField(max_length=250, blank=True, null=True)
  a2 = models.CharField(max_length=250, blank=True, null=True)
  a3 = models.CharField(max_length=250, blank=True, null=True)
  a4 = models.CharField(max_length=250, blank=True, null=True)
  a5 = models.CharField(max_length=250, blank=True, null=True)
  dream = models.CharField(max_length=250, blank=True, null=True)
  work = models.CharField(max_length=250, blank=True, null=True)

