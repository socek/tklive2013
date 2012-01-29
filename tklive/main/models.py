# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from scores.models import Place

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    
    default_place = models.ForeignKey(Place, verbose_name=u"Domyślna lokalizacja", null=True, blank=False)
    
    def __unicode__(self):
        return self.user.username
