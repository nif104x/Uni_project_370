from django import forms 
from django.core import validators
from django.core.exceptions import ValidationError

class textT(forms.Form):
    message = forms.CharField()
