# coding:utf-8

from django.conf.urls import patterns, include, url

from .views import list_artists, save_artist, list_albuns, list_songs, index, remove_artist

urlpatterns = patterns('',

	# Artist
	url(r'^artists/save/(\d+)', save_artist, name='save_artist'),
	url(r'^artists/remove/(\d+)', remove_artist, name='remove_artist'),
	url(r'^artists/', list_artists, name='list_artists'),

	# Album
    url(r'^albuns/(\d+)', list_albuns, name='list_albuns'),

    # Song
    url(r'^songs/(\d+)', list_songs, name='list_songs'),
	url(r'', index, name='pagina_inicial'),
)