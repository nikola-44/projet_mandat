from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreerUtilisateur

def inscriptionPage(request):
    form=CreerUtilisateur()
    if request.method=='POST':
        form=CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            return redirect('acces')
    context={'form':form}
    return render(request,'inscription.html', context)

def accesPage(request):
    context={}
    return render(request,'acces.html', context)

