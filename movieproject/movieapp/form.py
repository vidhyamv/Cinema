
from .models import Movie
from django import forms

class Movieform(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','desc','year','img']
