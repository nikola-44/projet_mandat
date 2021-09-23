from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Client



class CreerUtilisateur(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    dateNaissance = forms.DateField(label='dateNaissance', widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))

    class Meta:
        model = Client
        fields = ('nom', 'prenom', 'dateNaissance', 'telephone', 'genre')
