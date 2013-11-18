# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Day.work'
        db.alter_column(u'cities_users_day', 'work', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Day.a1'
        db.alter_column(u'cities_users_day', 'a1', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Day.a3'
        db.alter_column(u'cities_users_day', 'a3', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Day.a2'
        db.alter_column(u'cities_users_day', 'a2', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Day.a5'
        db.alter_column(u'cities_users_day', 'a5', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

        # Changing field 'Day.a4'
        db.alter_column(u'cities_users_day', 'a4', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))
        # Adding unique constraint on 'Day', fields ['date']
        db.create_unique(u'cities_users_day', ['date'])


        # Changing field 'Day.dream'
        db.alter_column(u'cities_users_day', 'dream', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

    def backwards(self, orm):
        # Removing unique constraint on 'Day', fields ['date']
        db.delete_unique(u'cities_users_day', ['date'])


        # Changing field 'Day.work'
        db.alter_column(u'cities_users_day', 'work', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'Day.a1'
        db.alter_column(u'cities_users_day', 'a1', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'Day.a3'
        db.alter_column(u'cities_users_day', 'a3', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'Day.a2'
        db.alter_column(u'cities_users_day', 'a2', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'Day.a5'
        db.alter_column(u'cities_users_day', 'a5', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'Day.a4'
        db.alter_column(u'cities_users_day', 'a4', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

        # Changing field 'Day.dream'
        db.alter_column(u'cities_users_day', 'dream', self.gf('django.db.models.fields.CharField')(default='', max_length=250))

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
            'a1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'a2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'a3': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'a4': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'a5': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'dream': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'work': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cities_users']