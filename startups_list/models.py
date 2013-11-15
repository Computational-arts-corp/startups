
from django.db import models
from django.utils import timezone

import datetime


# Create your models here.

class Startup(models.Model):
  name = models.CharField(max_length=256)
  website_url = models.CharField(max_length=256)
  descr = models.TextField()

  def __unicode__(self):
    return self.name

class Recruiter(models.Model):
  name = models.CharField(max_length=256)
  website_url = models.CharField(max_length=256)
  descr = models.TextField()

  def __unicode__(self):
    return self.name

class MediaOutlet(models.Model):
  name = models.CharField(max_length=256)
  website_url = models.CharField(max_length=256)
  descr = models.TextField()

  def __unicode__(self):
    return self.name
