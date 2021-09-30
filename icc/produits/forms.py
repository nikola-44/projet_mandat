#Dorian Châtelain
from django import forms
from .models import Produit


class Produit(forms.ModelForm):

    class Meta:
        model = Produit
        fields = ('nom', 'type', 'capacite', 'statut', 'quantite')