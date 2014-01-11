# coding=utf-8
from django.db import models

class Post(models.Model):
    name = models.CharField(max_length="30")
    msg = models.CharField(max_length="300")
  
    publishTime = models.DateTimeField(null=True)

    contentImg = models.FileField(upload_to='img/%Y/%m/%d', null=True)
    coverImg = models.FileField(upload_to='img/%Y/%m/%d', null=True)
  
    def __unicode__(self):
        return self.name + ": \"" + self.msg + "\""