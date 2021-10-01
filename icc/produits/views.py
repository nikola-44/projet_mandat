# Zumeri Faton et Châtelain Dorian
from django.shortcuts import render, redirect
from .models import Produit


# Create your views here.


def home(request):
    return render(request, 'produits.html')


def gererProduit(request):
    produits = Produit.objects.all()
    return render(request, '../templates/gererProduit.html', {'produits': produits})


def ajouter_produit(request):
    form = Produit()
    if request.method == 'POST':
        form = Produit(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/produits/gererProduits')
    context = {'form': form}
    return render(request, '../templates/ajouter_produit.html', context)


def supprimer_produit(request, pk):
    produit = Produit.objects.get(id=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('/produits/gererProduits')
    context = {'item': produit}
    return render(request, '../templates/supprimer_produit.html', context)
