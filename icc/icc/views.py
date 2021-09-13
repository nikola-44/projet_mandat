from django.shortcuts import render


def accueil(request):
    return render(request, 'accueil.html')


def contact(request):
    return render(request, 'contact.html')
