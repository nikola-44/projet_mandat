# Zumeri Faton et Châtelain Dorian
from django.shortcuts import render
from .models import Produit


# Create your views here.


def home(request):
    return render(request, 'produits.html')


def gererProduit(request):
    produits = Produit.objects.all()
    return render(request, '../templates/gererProduit.html', {'produits': produits})
