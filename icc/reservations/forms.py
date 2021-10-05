# FERREIRA STOJKOVIC Nikola

from django import forms
from . import models


class Rendezvous(forms.ModelForm):
    # date = forms.DateField()
    # heure = forms.TimeField()
    # commentaire = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = models.Reservation
        fields = ['date_heure', 'commentaire']
