from django.shortcuts import render, redirect


def accueil(request):
    return render(request, 'accueil.html')


def contact(request):
    return render(request, 'contact.html')


def coiffure(request):
    return render(request, 'coiffure.html')


def produits(request):
    return render(request, 'produits.html')


def acces(request):
    return render(request, 'acces.html')

