# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Team'
        db.create_table('scores_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('scores', ['Team'])

        # Adding model 'Player'
        db.create_table('scores_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scores.Team'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('staus', self.gf('django.db.models.fields.CharField')(default='player', max_length=10)),
        ))
        db.send_create_signal('scores', ['Player'])

        # Adding model 'Place'
        db.create_table('scores_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('scores', ['Place'])

        # Adding model 'Quart'
        db.create_table('scores_quart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team_1_points', self.gf('django.db.models.fields.IntegerField')()),
            ('team_2_points', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('scores', ['Quart'])

        # Adding model 'Tabel'
        db.create_table('scores_tabel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('scores', ['Tabel'])

        # Adding model 'Match'
        db.create_table('scores_match', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scores.Place'])),
            ('quart_1_d1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('quart_2_d1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('quart_3_d1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('quart_4_d1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('quart_1_d2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('quart_2_d2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('quart_3_d2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('quart_4_d2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('team_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='t1', to=orm['scores.Team'])),
            ('team_2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='t2', to=orm['scores.Team'])),
            ('tabel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scores.Tabel'])),
        ))
        db.send_create_signal('scores', ['Match'])


    def backwards(self, orm):
        
        # Deleting model 'Team'
        db.delete_table('scores_team')

        # Deleting model 'Player'
        db.delete_table('scores_player')

        # Deleting model 'Place'
        db.delete_table('scores_place')

        # Deleting model 'Quart'
        db.delete_table('scores_quart')

        # Deleting model 'Tabel'
        db.delete_table('scores_tabel')

        # Deleting model 'Match'
        db.delete_table('scores_match')


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
