from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
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
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect('accueil')

    return render(request,'acces.html', context)