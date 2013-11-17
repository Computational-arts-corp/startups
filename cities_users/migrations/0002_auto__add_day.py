# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Day'
        db.create_table(u'cities_users_day', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('a1', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('a2', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('a3', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('a4', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('a5', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('dream', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('work', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'cities_users', ['Day'])


    def backwards(self, orm):
        # Deleting model 'Day'
        db.delete_table(u'cities_users_day')


    models = {
        u'cities_users.addressbookitem': {
            'Meta': {'object_name': 'Addressbookitem'},
            'city_block': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cities_users.CityBlock']"}),
            'descr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'cities_users.cityblock': {
            'Meta': {'object_name': 'CityBlock'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'cities_users.day': {
            'Meta': {'object_name': 'Day'},
            'a1': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'a2': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'a3': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'a4': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'a5': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dream': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'work': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['cities_users']