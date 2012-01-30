# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
import scores.models as M

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        places = {
            'stas' : M.Place.objects.get(name=u'L.O. Staszic (Tarnowskie Góry)'),
            'radzionkow' : M.Place.objects.get(name=u'MOSIR (Radzionków)'),
        }
        tabels = {
            'a' : M.Tabel.objects.get(name=u'Grupa A'),
            'b' : M.Tabel.objects.get(name=u'Grupa B'),
            'f' : M.Tabel.objects.get(name=u'Finały'),
        }
        
        teams = {
            'przyjaciele': M.Team.objects.get(name=u'Przyjaciele szymona'),
            'nauczyciele': M.Team.objects.get(name=u'Nauczyciele'),
            'kutna': M.Team.objects.get(name=u'Kuta Hora'),
            'bekescaba': M.Team.objects.get(name=u'Bekescaba'),
            'bernburg': M.Team.objects.get(name=u'Bernburg'),
            'machina': M.Team.objects.get(name=u'MACHINA AG Rolbud'),
            'boguszow': M.Team.objects.get(name=u'Boguszów Gorce'),
            'serock': M.Team.objects.get(name=u'Serock'),
            'tgteam': M.Team.objects.get(name=u'T.G. Team'),
            'hef': M.Team.objects.get(name=u'HEF Lubliniec'),
        }

        loop = 0
        tabs = []
        tabs.append({
            'match_number'  : 1,
            'place'         : 'stas',
            'tabel'         : 'a',
            'tt1'           : 'przyjaciele',
            'tt2'           : 'kutna',
        })
        tabs.append({
            'match_number'  : 2,
            'place'         : 'stas',
            'tabel'         : 'a',
            'tt1'           : 'nauczyciele',
            'tt2'           : 'bekescaba',
        })
        
        tabs.append({
            'match_number'  : 3,
            'place'         : 'stas',
            'tabel'         : 'a',
            'tt1'           : 'przyjaciele',
            'tt2'           : 'bernburg',
        })
        
        tabs.append({
            'match_number'  : 4,
            'place'         : 'radzionkow',
            'tabel'         : 'b',
            'tt1'           : 'machina',
            'tt2'           : 'boguszow',
        })
        
        tabs.append({
            'match_number'  : 5,
            'place'         : 'radzionkow',
            'tabel'         : 'b',
            'tt1'           : 'serock',
            'tt2'           : 'tgteam',
        })
        
        tabs.append({
            'match_number'  : 6,
            'place'         : 'stas',
            'tabel'         : 'a',
            'tt1'           : 'nauczyciele',
            'tt2'           : 'kutna',
        })
        
        tabs.append({
            'match_number'  : 7,
            'place'         : 'stas',
            'tabel'         : 'a',
            'tt1'           : 'bekescaba',
            'tt2'           : 'bernburg',
        })
        
        tabs.append({
            'match_number'  : 8,
            'place'         : 'stas',
            'tabel'         : 'a',
            'tt1'           : 'nauczyciele',
            'tt2'           : 'przyjaciele',
        })
        
        tabs.append({
            'match_number'  : 9,
            'place'         : 'stas',
            'tabel'         : 'a',
            'tt1'           : 'kutna',
            'tt2'           : 'bekescaba',
        })
        
        tabs.append({
            'match_number'  : 10,
            'place'         : 'stas',
            'tabel'         : 'a',
            'tt1'           : 'nauczyciele',
            'tt2'           : 'bernburg',
        })
        
        tabs.append({
            'match_number'  : 11,
            'place'         : 'stas',
            'tabel'         : 'a',
            'tt1'           : 'bekescaba',
            'tt2'           : 'przyjaciele',
        })
        
        tabs.append({
            'match_number'  : 12,
            'place'         : 'stas',
            'tabel'         : 'a',
            'tt1'           : 'bernburg',
            'tt2'           : 'kutna',
        })
        
        tabs.append({
            'match_number'  : 13,
            'place'         : 'radzionkow',
            'tabel'         : 'b',
            'tt1'           : 'machina',
            'tt2'           : 'hef',
        })
        
        tabs.append({
            'match_number'  : 14,
            'place'         : 'radzionkow',
            'tabel'         : 'b',
            'tt1'           : 'boguszow',
            'tt2'           : 'serock',
        })
        
        tabs.append({
            'match_number'  : 15,
            'place'         : 'radzionkow',
            'tabel'         : 'b',
            'tt1'           : 'hef',
            'tt2'           : 'tgteam',
        })
        
        tabs.append({
            'match_number'  : 16,
            'place'         : 'radzionkow',
            'tabel'         : 'b',
            'tt1'           : 'machina',
            'tt2'           : 'serock',
        })
        
        tabs.append({
            'match_number'  : 17,
            'place'         : 'radzionkow',
            'tabel'         : 'b',
            'tt1'           : 'tgteam',
            'tt2'           : 'boguszow',
        })
        
        tabs.append({
            'match_number'  : 18,
            'place'         : 'radzionkow',
            'tabel'         : 'b',
            'tt1'           : 'hef',
            'tt2'           : 'serock',
        })
        
        tabs.append({
            'match_number'  : 19,
            'place'         : 'radzionkow',
            'tabel'         : 'b',
            'tt1'           : 'machina',
            'tt2'           : 'tgteam',
        })
        
        tabs.append({
            'match_number'  : 20,
            'place'         : 'radzionkow',
            'tabel'         : 'b',
            'tt1'           : 'boguszow',
            'tt2'           : 'hef',
        })
        
        tabs.append({
            'match_number'  : 21,
            'place'         : 'stas',
            'tabel'         : 'f',
        })
        
        tabs.append({
            'match_number'  : 22,
            'place'         : 'stas',
            'tabel'         : 'f',
        })
        
        tabs.append({
            'match_number'  : 23,
            'place'         : 'stas',
            'tabel'         : 'f',
        })
        
        tabs.append({
            'match_number'  : 24,
            'place'         : 'stas',
            'tabel'         : 'f',
        })
        
        for object in tabs:
            m = M.Match()
            m.match_number = object['match_number']
            m.place = places[ object['place'] ]
            m.tabel = tabels[ object['tabel'] ]
            if object.has_key('tt1'):
                m.team_1 = teams[ object['tt1'] ]
                m.team_2 = teams[ object['tt2'] ]
            m.save()

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
            'staus': ('django.db.models.fields.CharField', [], {'default': "'before'", 'max_length': '10'}),
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
