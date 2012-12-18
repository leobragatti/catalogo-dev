# coding: utf-8

from django.forms import ModelForm
from django import forms

from .models import Artist

class ArtistModelForm(ModelForm):
	error_css_class = 'error'
	required_css_class = 'required'

	class Meta:
		model = Artist


class ExampleForm(forms.Form):
	username = forms.CharField(max_length=30, label=u'Username')
	email = forms.EmailField(label=u'Email address')		