from django import forms 
from django.core import validators
from django.core.exceptions import ValidationError

def only_letter(value):
    if not all(x.isalpha() or x.isspace() for x in value):
        raise forms.ValidationError("Only letters are allowed!")
    
class registration(forms.Form):
    username = forms.CharField(
        validators=[
            validators.MaxLengthValidator(50),
            validators.MinLengthValidator(6)
        ]
    )

    password = forms.CharField(
        validators=[
            validators.MaxLengthValidator(255),
            validators.MinLengthValidator(8)
        ]
    )
    name = forms.CharField(
        validators=[
            validators.MaxLengthValidator(255),
            validators.MinLengthValidator(5),
            only_letter
        ]
    )

    email = forms.EmailField(
        max_length=255,
    )

class login_form(forms.Form):
    username = forms.CharField(
        validators=[
            validators.MaxLengthValidator(50),
            validators.MinLengthValidator(6)
        ]
    )

    password = forms.CharField(
        validators=[
            validators.MaxLengthValidator(255),
            validators.MinLengthValidator(8)
        ]
    )



