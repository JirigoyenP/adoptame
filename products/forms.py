from django import forms
from .models import Person


class RawProductForm(forms.Form):
	first_name = forms.CharField()
	last_name  = forms.CharField()
	image 	   = forms.ImageField()
