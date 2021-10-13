# FERREIRA STOJKOVIC Nikola
import datetime
from datetime import timedelta

from django.db import connection
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Reservation, Prestation, ResPres
from .forms import PrestationForm, ReservationForm
from django.contrib import messages


# Create your views here.

# PLANNING


def planning(request):
    # prestations = Prestation.objects.all()
    # ty = Prestation.LONGEUR_CHEVEUX
    #
    # types = []
    # for t in ty:
    #     (_, valeur) = t
    #     types.append(valeur)
    #
    # r_jour = Reservation.objects.all().filter(date_heure__date=datetime.date.today()).order_by('date_heure')
    # r_matin = r_jour.exclude(date_heure__time__gt='12:00:00')
    # print(r_matin)
    # for reservation in r_matin:
    #     print(reservation)
    # r_apresmidi = r_jour.exclude(date_heure__time__lt='12:00:00')
    #
    # return render(request, 'reservations/planning.html', {'r_matin': r_matin, 'r_apresmidi': r_apresmidi, 'types': types, 'prestations': prestations})
    reservations = Reservation.objects.all().order_by('-date_heure')
    return render(request, 'reservations/mes-reservations.html', {'reservations': reservations})


# @app.route('/reservations/<string:jour>', methods=['GET'])
def test(request):  # ajouter un paramètre jour
    prestations = Prestation.objects.all()
    ty = Prestation.LONGEUR_CHEVEUX

    types = []
    for t in ty:
        (_, valeur) = t
        types.append(valeur)
    print('Voici les types de cheveux: ' + str(type(types)), types)
    r_jour = Reservation.objects.all().filter(date_heure=datetime.date.today()).order_by('date_heure')
    r_matin = r_jour.exclude()
    r_apresmidi = r_jour.exclude()

    return render(request, 'reservations/test.html', {'r_matin': r_matin, 'r_apresmidi': r_apresmidi, 'prestations': prestations, 'types': types})


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


# ESPACE ADMIN


# RESERVATIONS


def ajouter_reservation(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        form.client = request.user
        if form.is_valid():
            form.save()
            return redirect('mes-reservations')
    return render(request, 'reservations/formulaire/reservation/ajouter-reservation.html', {'form': form})


def mes_reservations(request):
    res_pres = ResPres.objects.all()
    reservations = Reservation.objects.all().order_by('-date_heure')
    total = {}
    for reservation in reservations:
        calcul = 0
        for prestation in reservation.prestations.all():
            calcul += prestation.prix
        total[reservation.id] = calcul
    return render(request, 'reservations/mes-reservations.html', {'reservations': reservations, 'total': total, 'res_pres': res_pres})


# PRESTATIONS


def prestations_admin(request):
    prestation = Prestation.objects.all().order_by('nom', 'pour')
    return render(request, 'reservations/admin/prestations.html', {'prestations': prestation})


def ajouter_prestation(request):
    form = PrestationForm()
    if request.method == 'POST':
        form = PrestationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prestations-admin')
    return render(request, 'reservations/formulaire/prestation/ajouter-prestation.html', {'form': form})


def modifier_prestation(request, id):
    prestation = Prestation.objects.get(id=id)
    form = PrestationForm(instance=prestation)
    if request.method == 'POST':
        form = PrestationForm(request.POST, instance=prestation)
        if form.is_valid():
            form.save()
            return redirect('prestations-admin')
    return render(request, 'reservations/formulaire/prestation/modifier-prestation.html', {'form': form})


def supprimer_prestation(request, id):
    prestation = Prestation.objects.get(id=id)
    if request.method == 'POST':
        prestation.delete()
        return redirect('prestations-admin')
    return render(request, 'reservations/formulaire/prestation/supprimer-prestation.html', {'prestation': prestation})


def prestations(request):
    return render(request, 'reservations/prestations.html')
