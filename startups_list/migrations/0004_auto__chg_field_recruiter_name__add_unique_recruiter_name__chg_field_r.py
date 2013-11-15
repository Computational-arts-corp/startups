# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Recruiter.name'
        db.alter_column(u'startups_list_recruiter', 'name', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True))
        # Adding unique constraint on 'Recruiter', fields ['name']
        db.create_unique(u'startups_list_recruiter', ['name'])


        # Changing field 'Recruiter.website_url'
        db.alter_column(u'startups_list_recruiter', 'website_url', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True))
        # Adding unique constraint on 'Recruiter', fields ['website_url']
        db.create_unique(u'startups_list_recruiter', ['website_url'])


        # Changing field 'Startup.name'
        db.alter_column(u'startups_list_startup', 'name', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True))
        # Adding unique constraint on 'Startup', fields ['name']
        db.create_unique(u'startups_list_startup', ['name'])


        # Changing field 'Startup.website_url'
        db.alter_column(u'startups_list_startup', 'website_url', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True))
        # Adding unique constraint on 'Startup', fields ['website_url']
        db.create_unique(u'startups_list_startup', ['website_url'])


        # Changing field 'MediaOutlet.name'
        db.alter_column(u'startups_list_mediaoutlet', 'name', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True))
        # Adding unique constraint on 'MediaOutlet', fields ['name']
        db.create_unique(u'startups_list_mediaoutlet', ['name'])


        # Changing field 'MediaOutlet.website_url'
        db.alter_column(u'startups_list_mediaoutlet', 'website_url', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True))
        # Adding unique constraint on 'MediaOutlet', fields ['website_url']
        db.create_unique(u'startups_list_mediaoutlet', ['website_url'])


    def backwards(self, orm):
        # Removing unique constraint on 'MediaOutlet', fields ['website_url']
        db.delete_unique(u'startups_list_mediaoutlet', ['website_url'])

        # Removing unique constraint on 'MediaOutlet', fields ['name']
        db.delete_unique(u'startups_list_mediaoutlet', ['name'])

        # Removing unique constraint on 'Startup', fields ['website_url']
        db.delete_unique(u'startups_list_startup', ['website_url'])

        # Removing unique constraint on 'Startup', fields ['name']
        db.delete_unique(u'startups_list_startup', ['name'])

        # Removing unique constraint on 'Recruiter', fields ['website_url']
        db.delete_unique(u'startups_list_recruiter', ['website_url'])

        # Removing unique constraint on 'Recruiter', fields ['name']
        db.delete_unique(u'startups_list_recruiter', ['name'])


        # Changing field 'Recruiter.name'
        db.alter_column(u'startups_list_recruiter', 'name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Recruiter.website_url'
        db.alter_column(u'startups_list_recruiter', 'website_url', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Startup.name'
        db.alter_column(u'startups_list_startup', 'name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'Startup.website_url'
        db.alter_column(u'startups_list_startup', 'website_url', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'MediaOutlet.name'
        db.alter_column(u'startups_list_mediaoutlet', 'name', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

        # Changing field 'MediaOutlet.website_url'
        db.alter_column(u'startups_list_mediaoutlet', 'website_url', self.gf('django.db.models.fields.CharField')(max_length=256, null=True))

    models = {
        u'startups_list.mediaoutlet': {
            'Meta': {'object_name': 'MediaOutlet'},
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'startups_list.recruiter': {
            'Meta': {'object_name': 'Recruiter'},
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'startups_list.startup': {
            'Meta': {'object_name': 'Startup'},
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['startups_list']