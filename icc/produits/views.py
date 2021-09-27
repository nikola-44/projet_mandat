from django.shortcuts import render

# Create your views here.
from icc.produits.models import Produit


def produits(request, pk):
    if request.method == "POST":
        produits = Produit()
        nom = request.POST.get('nom')
        type = request.POST.get('type')
        image = request.POST.get('image')
        capacite = request.POST.get('capacite')
        statut = request.POST.get('statut')
    return render(request, 'gererProduit')



