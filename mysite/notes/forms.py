from django import forms
from django.forms import ModelForm
from .models import *

class newNote(ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'