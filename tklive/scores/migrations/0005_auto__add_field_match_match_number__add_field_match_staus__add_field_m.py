# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Match.match_number'
        db.add_column('scores_match', 'match_number', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Match.staus'
        db.add_column('scores_match', 'staus', self.gf('django.db.models.fields.CharField')(default='before', max_length=10), keep_default=False)

        # Adding field 'Match.date'
        db.add_column('scores_match', 'date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now()), keep_default=False)

        # Changing field 'Match.team_1'
        db.alter_column('scores_match', 'team_1_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['scores.Team']))

        # Changing field 'Match.team_2'
        db.alter_column('scores_match', 'team_2_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['scores.Team']))


    def backwards(self, orm):
        
        # Deleting field 'Match.match_number'
        db.delete_column('scores_match', 'match_number')

        # Deleting field 'Match.staus'
        db.delete_column('scores_match', 'staus')

        # Deleting field 'Match.date'
        db.delete_column('scores_match', 'date')

        # User chose to not deal with backwards NULL issues for 'Match.team_1'
        raise RuntimeError("Cannot reverse this migration. 'Match.team_1' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Match.team_2'
        raise RuntimeError("Cannot reverse this migration. 'Match.team_2' and its values cannot be restored.")


    models = {
        'scores.match': {
            'Meta': {'object_name': 'Match'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match_number': ('django.db.models.fields.IntegerField', [], {}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['scores.Place']"}),
            'quart_1_d1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quart_1_d2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quart_2_d1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quart_2_d2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quart_3_d1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quart_3_d2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quart_4_d1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'quart_4_d2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
