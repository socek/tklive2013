# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from main.models import Place

# Create your models here.

class Post(models.Model):
    text = models.CharField(u'treść', max_length=255)
    place = models.ForeignKey(Place, null=True)
    pub_date = models.DateTimeField(u'data publikacji', auto_now_add=True)
    author = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.text
