# FERREIRA STOJKOVIC Nikola

from django import forms
from . import models


class Rendezvous(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = ['date_heure', 'commentaire']
