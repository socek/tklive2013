# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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
    
    team_1 = models.ForeignKey(Team, related_name='t1')
    team_2 = models.ForeignKey(Team, related_name='t2')



class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    
    default_place = models.ForeignKey(Place, verbose_name=u"Domyślna lokalizacja", null=True, blank=False)
    
    def __unicode__(self):
        return self.user.username

#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        UserProfile.objects.create(user=instance)
#
#post_save.connect(create_user_profile, sender=User)
