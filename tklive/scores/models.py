# -*- encoding: utf-8 -*-
from django.db import models

class Team(models.Model):
    name = models.CharField(u'Nazwa', max_length=100)

    def __unicode__(self):
        return self.name
    
player_status=(
    ('player', 'Gracz'),
    ('couch', 'Trener'),
)

class Player(models.Model):
    team = models.ForeignKey(Team)
    name = models.CharField(u'Nazwa', max_length=100)
    surname = models.CharField(u'Nazwisko', max_length=100)
    number = models.IntegerField(u'Numer', blank=True, null=True)
    staus = models.CharField(u'Typ', max_length=10, choices=player_status, default='player')

class Place(models.Model):
    name = models.CharField(u'Nazwa', max_length=100)
    
    def __unicode__(self):
        return self.name

class Quart(models.Model):
    team_1_points = models.IntegerField(u'Punkty drużyny 1')
    team_2_points = models.IntegerField(u'Punkty drużyny 2')

    def __unicode__(self):
        return self.name

class Tabel(models.Model):
    name = models.CharField(u'Tabela', max_length=50)
    
    def __unicode__(self):
        return self.name
    
    def get_nicename(self):
        return self.name.replace(' ','_').replace(u'ł', 'l').lower()
    
class Highscore(models.Model):
    number = models.IntegerField(u'Miejsce')
    team = models.OneToOneField(Team, unique=True,)

match_status = (
    ('before', u'Nie rozpoczęto'),
    ('actual', u'W trakcie'),
    ('finished', u'Zakończony'),
)

class Match(models.Model):
    place = models.ForeignKey(Place)
    
    quart_1_d1 = models.IntegerField('Drużyna 1', blank=True, null=True)
    quart_2_d1 = models.IntegerField('Drużyna 1', blank=True, null=True)
    quart_3_d1 = models.IntegerField('Drużyna 1', blank=True, null=True)
    quart_4_d1 = models.IntegerField('Drużyna 1', blank=True, null=True)
    
    quart_1_d2 = models.IntegerField('Drużyna 2', blank=True, null=True)
    quart_2_d2 = models.IntegerField('Drużyna 2', blank=True, null=True)
    quart_3_d2 = models.IntegerField('Drużyna 2', blank=True, null=True)
    quart_4_d2 = models.IntegerField('Drużyna 2', blank=True, null=True)
    
    team_1 = models.ForeignKey(Team, related_name='t1', blank=True, null=True)
    team_2 = models.ForeignKey(Team, related_name='t2', blank=True, null=True)
    
    tabel = models.ForeignKey(Tabel)
    
    match_number = models.IntegerField('Numer meczu', default=0)
    
    staus = models.CharField(u'Status', max_length=10, choices=match_status, default='before')
    date = models.DateTimeField(u'data meczu')
    
    @property
    def team1_result(self):
        return self.get_result()[0]
    
    @property
    def team2_result(self):
        return self.get_result()[1]
    
    def get_team_data(self, team):
        result = self.get_result()
        if team == self.team_1:
            me = 0
            enemy = 1
        elif team == self.team_2:
            me = 1
            enemy = 0
        
        tab = {
            'points' : result[me],
        }
        
        if result[me] > result[enemy]:
            tab['status'] = 'win'
        elif result[me] == result[enemy]:
            tab['status'] = 'draw'
        else:
            tab['status'] = 'lose'
        
        return tab
    
    def get_result(self):
        t1_result = 0
        if self.quart_1_d1 != None:
            t1_result += self.quart_1_d1
            if self.quart_2_d1 != None:
                t1_result += self.quart_2_d1
                if self.quart_3_d1 != None:
                    t1_result += self.quart_3_d1
                    if self.quart_4_d1 != None:
                        t1_result += self.quart_4_d1
        t2_result = 0
        if self.quart_1_d2 != None:
            t2_result += self.quart_1_d2
            if self.quart_2_d2 != None:
                t2_result += self.quart_2_d2
                if self.quart_3_d2 != None:
                    t2_result += self.quart_3_d2
                    if self.quart_4_d2 != None:
                        t2_result += self.quart_4_d2
        return t1_result, t2_result
