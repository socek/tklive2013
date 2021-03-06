# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Match.quart_4_d2'
        db.alter_column('scores_match', 'quart_4_d2', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Match.quart_2_d2'
        db.alter_column('scores_match', 'quart_2_d2', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Match.quart_1_d1'
        db.alter_column('scores_match', 'quart_1_d1', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Match.quart_1_d2'
        db.alter_column('scores_match', 'quart_1_d2', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Match.quart_3_d1'
        db.alter_column('scores_match', 'quart_3_d1', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Match.quart_3_d2'
        db.alter_column('scores_match', 'quart_3_d2', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Match.quart_2_d1'
        db.alter_column('scores_match', 'quart_2_d1', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Match.quart_4_d1'
        db.alter_column('scores_match', 'quart_4_d1', self.gf('django.db.models.fields.IntegerField')())


    def backwards(self, orm):
        
        # Changing field 'Match.quart_4_d2'
        db.alter_column('scores_match', 'quart_4_d2', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Match.quart_2_d2'
        db.alter_column('scores_match', 'quart_2_d2', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Match.quart_1_d1'
        db.alter_column('scores_match', 'quart_1_d1', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Match.quart_1_d2'
        db.alter_column('scores_match', 'quart_1_d2', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Match.quart_3_d1'
        db.alter_column('scores_match', 'quart_3_d1', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Match.quart_3_d2'
        db.alter_column('scores_match', 'quart_3_d2', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Match.quart_2_d1'
        db.alter_column('scores_match', 'quart_2_d1', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Match.quart_4_d1'
        db.alter_column('scores_match', 'quart_4_d1', self.gf('django.db.models.fields.IntegerField')(null=True))


    models = {
        'scores.highscore': {
            'Meta': {'object_name': 'Highscore'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'team': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['scores.Team']", 'unique': 'True'})
        },
        'scores.match': {
            'Meta': {'object_name': 'Match'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scores.Place']"}),
            'quart_1_d1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quart_1_d2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quart_2_d1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quart_2_d2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quart_3_d1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quart_3_d2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quart_4_d1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quart_4_d2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'staus': ('django.db.models.fields.CharField', [], {'default': "'before'", 'max_length': '10'}),
            'tabel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scores.Tabel']"}),
            'team_1': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'t1'", 'null': 'True', 'to': "orm['scores.Team']"}),
            'team_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'t2'", 'null': 'True', 'to': "orm['scores.Team']"})
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
