# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
import scores.models as M

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        for tab in [{
            'name' : u'Grupa A',
        },{
            'name' : u'Grupa B',
        },{
            'name' : u'Finały',
        }]:
            tabel = M.Tabel(**tab)
            tabel.save()

    def backwards(self, orm):
        "Write your backwards methods here."


    models = {
        'scores.match': {
            'Meta': {'object_name': 'Match'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scores.Place']"}),
            'quart_1_d1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quart_1_d2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quart_2_d1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quart_2_d2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quart_3_d1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quart_3_d2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quart_4_d1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quart_4_d2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tabel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scores.Tabel']"}),
            'team_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'t1'", 'to': "orm['scores.Team']"}),
            'team_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'t2'", 'to': "orm['scores.Team']"})
        },
        'scores.place': {
            'Meta': {'object_name': 'Place'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'scores.player': {
            'Meta': {'object_name': 'Player'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'staus': ('django.db.models.fields.CharField', [], {'default': "'player'", 'max_length': '10'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scores.Team']"})
        },
        'scores.quart': {
            'Meta': {'object_name': 'Quart'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team_1_points': ('django.db.models.fields.IntegerField', [], {}),
            'team_2_points': ('django.db.models.fields.IntegerField', [], {})
        },
        'scores.tabel': {
            'Meta': {'object_name': 'Tabel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'scores.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['scores']
