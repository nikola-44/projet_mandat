# Dorian Châtelain

from django import forms
from .models import Parametres


class SalonForm(forms.ModelForm):
    class Meta:
        model = Parametres
        fields = ['stockMinPVente', 'prixLivraison', 'telephone', 'adresse','codePostal','mail', 'nomSalon']
