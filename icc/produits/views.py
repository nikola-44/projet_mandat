# Zumeri Faton et Châtelain Dorian
from django.shortcuts import render, redirect
from .forms import ProduitForm
from .models import Produit
from django.views import View
from django.http import JsonResponse
import json



# Create your views here.


def home(request):
    produits = Produit.objects.all()
    print(produits)
    context = {'produits': produits}
    return render(request, 'produits.html', context)


def cart(request):
    context = {}
    return render(request, 'cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)


def gererProduit(request):
    produits = Produit.objects.all()
    return render(request, '../templates/gererProduit.html', {'produits': produits})


def ajouter_produit(request):
    if request.method == "POST":
        fm = ProduitForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/produits/gererProduits')
    else:
        fm = ProduitForm()
    return render(request, '../templates/ajouter_produit.html', {'form': fm})


def modifier_produit(request, pk):
    if request.method == 'POST':
        pi = Produit.objects.get(id=pk)
        fm = ProduitForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/produits/gererProduits')
    else:
        pi = Produit.objects.get(id=pk)
        fm = ProduitForm(instance=pi)
    return render(request, '../templates/modifier_produit.html', {'form': fm})


def supprimer_produit(request, pk):
    produit = Produit.objects.get(id=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('/produits/gererProduits')
    context = {'item': produit}
    return render(request, '../templates/supprimer_produit.html', context)


def updateItem(request):
    data = json.loads(request.body)
    produitId = data['produitId']
    action = data['action']

    print('Action:', action)
    print('produitId:', produitId)

    # Produit = Produit.objects.get(id=produitId)
    return JsonResponse('Item was added', safe=False)

