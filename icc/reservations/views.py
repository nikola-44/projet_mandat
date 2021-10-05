# FERREIRA STOJKOVIC Nikola
import datetime
from datetime import timedelta

from django.db import connection
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from . import forms
from .models import Reservation, Prestation
from django.contrib import messages


# Create your views here.

# PLANNING


# @login_required(login_url='acces')
# def planning_visiteurs(request):
#
#     r_jour = Reservation.objects.all().filter(date_heure__date=datetime.date.today()).order_by('date_heure')
#     r_matin = r_jour.exclude(date_heure__time__gt='12:00:00')
#     print(r_matin)
#     for reservation in r_matin:
#         print(reservation)
#     r_apresmidi = r_jour.exclude(date_heure__time__lt='12:00:00')
#
#     return render(request, 'reservations/planning-visiteurs.html', {'r_matin': r_matin, 'r_apresmidi': r_apresmidi})
#
#
# def planning_clients(request):
#     return render(request, 'reservations/planning-clients.html')


def planning(request):
    prestations = Prestation.objects.all()
    ty = Prestation.LONGEUR_CHEVEUX

    types = []
    for t in ty:
        (_, valeur) = t
        types.append(valeur)

    r_jour = Reservation.objects.all().filter(date_heure__date=datetime.date.today()).order_by('date_heure')
    r_matin = r_jour.exclude(date_heure__time__gt='12:00:00')
    print(r_matin)
    for reservation in r_matin:
        print(reservation)
    r_apresmidi = r_jour.exclude(date_heure__time__lt='12:00:00')

    return render(request, 'reservations/planning.html', {'r_matin': r_matin, 'r_apresmidi': r_apresmidi, 'types': types, 'prestations': prestations})


def rendezvous(request):
    if request.method == 'POST':
        form = forms.Rendezvous(request.POST)
        if form.is_valid():
            # rdv = form.save(commit=False)
            # rdv.utilisateur = request.user
            # rdv.save()
            form.save()
            messages.success(request, "Votre réservation a bien été enregistrée!")
            return redirect('planning')
    else:
        form = forms.Rendezvous()
    return render(request, 'reservations/reserver.html', {'form': form})


# @app.route('/reservations/<string:jour>', methods=['GET'])
# def test(request, jour):  # ajouter un paramètre jour
#     prestations = Prestation.objects.all()
#     ty = Prestation.LONGEUR_CHEVEUX
#
#     types = []
#     for t in ty:
#         (_, valeur) = t
#         types.append(valeur)
#     print('Voici les types de cheveux: ' + str(type(types)), types)
#     r_jour = Reservation.objects.all().filter(date=datetime.date.today() + datetime.timedelta(days=jour)).order_by('heure')
#     r_matin = r_jour.exclude(heure__gt='12:00:00')
#     r_apresmidi = r_jour.exclude(heure__lt='12:00:00')
#
#     return render(request, 'reservations/test.html', {'r_matin': r_matin, 'r_apresmidi': r_apresmidi, 'prestations': prestations, 'types': types})


# @receiver(pre_save, sender=Reservation)
# def verification(sender, **kwargs):
#     reservation = kwargs['instance']
#     print('sender: ', sender)
# pas de return


def test_prestations(request):
    prestations = Prestation.objects.all()

    noms = []
    for prestation in prestations:
        if prestation.pour != '/':
            if prestation.nom in noms:
                pass
            else:
                noms.append(prestation.nom)
    # print(noms)

    prix = []

    for nom in noms:
        objects = Prestation.objects.all().filter(nom=nom)
        p = []
        for o in objects:
            p.append(o.prix)
        tup = tuple(p)
        # print(nom)
        # print(tup)
        # print(nom + ' - ' + tup.__str__())
        prix.append(tup)
    # print(prix)

    dico = {}
    cpt = 0
    for nom in noms:
        dico[noms[cpt]] = (prix[cpt])
        cpt += 1
    print(dico)

    return render(request, 'reservations/test-prestations.html', {'prestations': prestations, 'dico': dico})


# def reserver(request):
#     if request.method == 'POST':
#         form = Reservation(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Réservation réussie!')
#     else:
#         form = Reservation()
#     return render(request, 'reservations/planning-visiteurs.html', {'form': form})


def prestations(request):
    return render(request, 'reservations/prestations.html')
