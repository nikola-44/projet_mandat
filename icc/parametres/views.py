# Nikola Stojkovic Dorian Châtelain
from django.shortcuts import render, redirect

# Create your views here.
from .forms import SalonForm
from .models import Parametres


def gererSalon(request):
    print(Parametres.objects.all())
    if request.method == 'POST':
        pi = Parametres.objects.get(id=17)
        fm = SalonForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('.')
    else:
        print(Parametres.objects.all())
        pi = Parametres.objects.get(id=17)
        fm = SalonForm(instance=pi)
    return render(request, '../templates/gererSalon.html', {'form': fm})


# def modifier_produit(request, pk):
#     if request.method == 'POST':
#         pi = Produit.objects.get(id=pk)
#         fm = ProduitForm(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#             return redirect('/produits/gererProduits')
#     else:
#         pi = Produit.objects.get(id=pk)
#         fm = ProduitForm(instance=pi)
#     return render(request, '../templates/modifier_produit.html', {'form': fm})
