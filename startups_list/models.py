
from django.db import models
from django.utils import timezone

import datetime


# Create your models here.

class Startup(models.Model):
  name = models.CharField( max_length=200, null=True, blank=True, unique=True )
  website_url = models.CharField( max_length=200, null=True, blank=True )
  descr = models.TextField( null=True, blank=True )
  city_name = models.CharField(max_length=200, null=True, blank=True )
  
  has_vacancy = models.BooleanField( default=True )
  has_applied = models.BooleanField( default=False )

  applied_on = models.DateField( 'applied on', blank=True, null=True )

  def __unicode__(self):
    return self.name

class Recruiter(models.Model):
  name = models.CharField(max_length=200, null=True, blank=True, unique=True )
  website_url = models.CharField(max_length=200, null=True, blank=True, unique=False )
  descr = models.TextField(null=True, blank=True )

  def __unicode__(self):
    return self.name

class MediaOutlet(models.Model):
  name = models.CharField(max_length=200, null=True, blank=True, unique=True )
  website_url = models.CharField(max_length=200, null=True, blank=True ) 
  descr = models.TextField(null=True, blank=True)

  def __unicode__(self):
    return self.name
