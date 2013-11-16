# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CityBlock'
        db.create_table(u'cities_users_cityblock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'cities_users', ['CityBlock'])

        # Adding model 'Addressbookitem'
        db.create_table(u'cities_users_addressbookitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True, blank=True)),
            ('descr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('city_block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cities_users.CityBlock'])),
        ))
        db.send_create_signal(u'cities_users', ['Addressbookitem'])


    def backwards(self, orm):
        # Deleting model 'CityBlock'
        db.delete_table(u'cities_users_cityblock')

        # Deleting model 'Addressbookitem'
        db.delete_table(u'cities_users_addressbookitem')


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
        }
    }

    complete_apps = ['cities_users']