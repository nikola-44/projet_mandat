# Zumeri Faton et Châtelain Dorian
from django import forms
from .models import Produit


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'type', 'capacite', 'prix_achat', 'prix_vente', 'statut', 'quantite']
        choix = (
            ("En vente", "En vente"),
            ("Pas en vente", "Pas en vente"),
        )
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'capacite': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'prix_achat': forms.TextInput(attrs={'class': 'form-control'}),
            'prix_vente': forms.TextInput(attrs={'class': 'form-control'}),
            'statut': forms.Select(choices=choix, attrs={'class': 'form-control'}),
            'quantite': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
        }