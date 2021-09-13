from django.shortcuts import render
from django.views.generic import ListView, DetailView


def accueil(request):
    return render(request, 'accueil.html')


def contact(request):
    return render(request, 'contact.html')
