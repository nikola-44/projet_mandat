from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import CreerUtilisateur
from django.contrib import messages



def inscriptionPage(request):
    form = CreerUtilisateur()
    if request.method == 'POST':
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Compte Créer avec succès, Bienvenue '+user)
            return redirect('acces')
    context = {'form': form}
    return render(request, 'inscription.html', context)


def accesPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            messages.info(request,"Utilisateur ou mot de passe invalide")

    return render(request, 'acces.html', context)

def logoutUser(request):
    logout(request)
    return redirect('accueil')
