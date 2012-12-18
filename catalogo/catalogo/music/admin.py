# coding: utf-8
from django.contrib import admin
from .models import Artist, Album, Song

class AlbumInline(admin.StackedInline):
    model = Album
    extra = 1

class SongInline(admin.StackedInline):
    model = Song
    extra = 1

#class CreditoInline(admin.TabularInline):
#    model = Credito

class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        SongInline,
    ]

class ArtistAdmin(admin.ModelAdmin):
	inlines = [
		AlbumInline
	]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song)
