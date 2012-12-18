# coding: UTF-8
from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=128)
    
    class Meta:
        db_table = 'Artist'
    
    def __unicode__(self):
        return self.name
    
class Album(models.Model):
    name = models.CharField(max_length=256)
    artist = models.ForeignKey(Artist)
    year = models.PositiveIntegerField()

    class Meta:
        db_table = 'Album'
    
    def __unicode__(self):
        return self.name
    
class Song(models.Model):
    album = models.ForeignKey(Album)
    name = models.CharField(max_length=256)
    number = models.PositiveSmallIntegerField()
    length = models.TimeField(null=True)
    lyrics = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Song'
    
    def __unicode__(self):
        return self.name
