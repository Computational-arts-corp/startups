from django.db import models
from django.utils import timezone

from cities_users.models import City

import datetime

class Startup(models.Model):
  name = models.CharField( max_length=200, null=True, blank=True, unique=True )
  website_url = models.CharField( max_length=200, null=True, blank=True )
  descr = models.TextField( null=True, blank=True )

  city = models.ForeignKey(City, blank=True,null=True)

  has_vacancy = models.BooleanField( default=True )
  has_applied = models.BooleanField( default=False )
  applied_on = models.DateField( 'applied on', blank=True, null=True )

  is_dead = models.BooleanField( default=False )

  @classmethod
  def list_pursuitable(self):
    all_startups = Startup.objects.all()
    out = []
    for s in all_startups:
      if s.has_vacancy and (not s.is_dead) and (not s.has_applied):
        out.append( s )
    return out

  def is_pursuitable(self):
    return self.has_vacancy and (not self.is_dead) and (not self.has_applied)
  # is_pursuitable.admin_order_field = 'is_dead'
  is_pursuitable.boolean = True
  is_pursuitable.short_description = 'Pursuitable?'

  def __unicode__(self):
    return self.name

class Recruiter(models.Model):
  name = models.CharField(max_length=200, null=True, blank=True, unique=True )
  website_url = models.CharField(max_length=200, null=True, blank=True, unique=False )
  descr = models.TextField(null=True, blank=True )

  has_applied = models.BooleanField( default=False )
  applied_on = models.DateField( 'applied on', blank=True, null=True )

  city = models.ForeignKey(City, blank=True,null=True)

  def __unicode__(self):
    return self.name

class MediaOutlet(models.Model):
  name = models.CharField(max_length=200, null=True, blank=True, unique=True )
  website_url = models.CharField(max_length=200, null=True, blank=True ) 
  descr = models.TextField(null=True, blank=True)

  def __unicode__(self):
    return self.name
