# coding: utf-8
from .models import Artist, Album, Song
from .forms import ArtistModelForm, ExampleForm

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse

def artist_item(artist):
	item = u"""<li id=\"artist{id}_header\">
				<h2>
					<a class=\"artist\" href=\"#\" id=\"artist{id}\" name=\"{url_albuns}\">{name}</a>	
					<a class=\"artist-edit\" id=\"{id}\" name=\"{url_save}\" href=\"#\"><img src="{static}images/edit.png"</img></a>
					<a class=\"artist-remove\" id=\"{id}\" name=\"{url_remove}\" href=\"#\"><img src="{static}images/delete.png"</img></a>
				</h2>
				<ul id=\"artist{id}_list\"></ul>
			</li>"""
	return item.format(id=artist.id, 
					  name=artist.name,
					  url_albuns=reverse('list_albuns', args=[artist.id]),
					  url_save=reverse('save_artist', args=[artist.id]),
					  url_remove=reverse('remove_artist', args=[artist.id]),
					  static=settings.STATIC_URL)

def index(request):
	return render(request, 'music/index.html')

def list_artists(request):
	items = Artist.objects.all().order_by('name')
	vars_template = {'artists': items}
	return render(request, 'music/artists.html', vars_template)

def list_albuns(request, artist_id):
	albuns = Album.objects.filter(artist_id = artist_id).order_by('year')
	vars_template = {'albuns': albuns, 'artist_id': artist_id}
	return render(request, 'music/albuns.html', vars_template)

def list_songs(request, album_id):
	songs = Song.objects.filter(album_id = album_id).order_by('number')
	vars_template = {'songs': songs}
	return render(request, 'music/songs.html', vars_template)

def save_artist(request, artist_id):
	#import pdb; pdb.set_trace()
	try:
		a = Artist.objects.get(pk=artist_id)
	except Artist.DoesNotExist as e:
		a = Artist()

	if request.method == 'POST':
		formulario = ArtistModelForm(request.POST, prefix="saveArtist", instance=a)
		if formulario.is_valid():
			formulario.save()
			url = reverse('list_albuns', args=[a.id])
			url_save = reverse('save_artist', args=[a.id])
			return HttpResponse(artist_item(a))
		else:
			vars_template = {'formulario': formulario, 'artist_id': artist_id}
			return render(request, 'music/editar_artist.html', vars_template)
	else:
		formulario = ArtistModelForm(prefix="saveArtist", auto_id='%s', instance=a)
		vars_template = {'formulario': formulario, 'artist_id': artist_id}
		return render(request, 'music/editar_artist.html', vars_template)

def remove_artist(request, artist_id):
	try:
		a = Artist.objects.get(pk=artist_id)
	except Artist.DoesNotExist as e:
		a = Artist()
		
	return render(request, 'music/remove_artist.html', {'artist_id': artist_id})