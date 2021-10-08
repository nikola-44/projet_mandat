# FERREIRA STOJKOVIC Nikola
from django import forms
from django.forms import ModelForm
from .models import Prestation, Reservation


# class Rendezvous(forms.ModelForm):
#     # date = forms.DateField()
#     # heure = forms.TimeField()
#     # commentaire = forms.CharField(widget=forms.Textarea())
#
#     class Meta:
#         model = models.Reservation
#         fields = ['date_heure', 'commentaire']


class PrestationForm(ModelForm):
    class Meta:
        model = Prestation
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'pour': forms.Select(attrs={'class': 'form-control'}),
            'prix': forms.TextInput(attrs={'class': 'form-control', 'type': 'decimal'}),
            'duree': forms.TextInput(attrs={'class': 'form-control', 'type': 'time', 'value': '00:00', 'step': '300'}),
        }


class ReservationsForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
