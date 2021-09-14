from django.shortcuts import render

def inscriptionPage(request):
    context={}
    return render(request,'inscription.html', context)

def accesPage(request):
    context={}
    return render(request,'acces.html', context)
# Create your views here.
