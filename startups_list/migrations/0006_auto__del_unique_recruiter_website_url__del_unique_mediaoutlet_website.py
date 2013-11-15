# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'MediaOutlet', fields ['website_url']
        db.delete_unique(u'startups_list_mediaoutlet', ['website_url'])

        # Removing unique constraint on 'Recruiter', fields ['website_url']
        db.delete_unique(u'startups_list_recruiter', ['website_url'])


    def backwards(self, orm):
        # Adding unique constraint on 'Recruiter', fields ['website_url']
        db.create_unique(u'startups_list_recruiter', ['website_url'])

        # Adding unique constraint on 'MediaOutlet', fields ['website_url']
        db.create_unique(u'startups_list_mediaoutlet', ['website_url'])


    models = {
        u'startups_list.mediaoutlet': {
            'Meta': {'object_name': 'MediaOutlet'},
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'startups_list.recruiter': {
            'Meta': {'object_name': 'Recruiter'},
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'startups_list.startup': {
            'Meta': {'object_name': 'Startup'},
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['startups_list']