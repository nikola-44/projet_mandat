from django.shortcuts import render


def accueil(request):
    return render(request, 'accueil.html')


def produits(request):
    return render(request, 'produits.html')


def acces(request):
    return render(request, 'acces.html')
