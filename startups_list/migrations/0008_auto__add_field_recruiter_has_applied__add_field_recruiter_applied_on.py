# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Recruiter.has_applied'
        db.add_column(u'startups_list_recruiter', 'has_applied',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Recruiter.applied_on'
        db.add_column(u'startups_list_recruiter', 'applied_on',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Recruiter.has_applied'
        db.delete_column(u'startups_list_recruiter', 'has_applied')

        # Deleting field 'Recruiter.applied_on'
        db.delete_column(u'startups_list_recruiter', 'applied_on')


    models = {
        u'cities_users.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'startups_list.mediaoutlet': {
            'Meta': {'object_name': 'MediaOutlet'},
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'startups_list.recruiter': {
            'Meta': {'object_name': 'Recruiter'},
            'applied_on': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_users.City']", 'null': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'has_applied': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'startups_list.startup': {
            'Meta': {'object_name': 'Startup'},
            'applied_on': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'has_applied': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_vacancy': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_dead': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['startups_list']