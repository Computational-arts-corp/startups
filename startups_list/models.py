
from django.db import models
from django.utils import timezone

import datetime


# Create your models here.

class Startup(models.Model):
  name = models.CharField(max_length=256, null=True, blank=True)
  website_url = models.CharField(max_length=256, null=True, blank=True)
  descr = models.TextField(null=True, blank=True)

  def __unicode__(self):
    return self.name

class Recruiter(models.Model):
  name = models.CharField(max_length=256, null=True, blank=True)
  website_url = models.CharField(max_length=256, null=True, blank=True)
  descr = models.TextField(null=True, blank=True)

  def __unicode__(self):
    return self.name

class MediaOutlet(models.Model):
  name = models.CharField(max_length=256, null=True, blank=True)
  website_url = models.CharField(max_length=256, null=True, blank=True)
  descr = models.TextField(null=True, blank=True)

  def __unicode__(self):
    return self.name
