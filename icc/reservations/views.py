import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Reservation, Prestation
# Create your views here.


# @login_required(login_url='acces')
def planning(request):
    return render(request, 'reservations/planning.html')


# @app.route('/reservations/<string:jours>', methods=['GET'])
def test(request, jours):
    r = Reservation.objects.all().filter(date=jours).order_by('heure')
    r_matin = r.exclude(heure__gt='12:00:00')
    r_apresmidi = r.exclude(heure__lt='12:00:00')
    return render(request, 'reservations/test.html', {'r_matin': r_matin, 'r_apresmidi': r_apresmidi})


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


def reserver(request):
    if request.method == 'POST':
        form = Reservation(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Réservation réussie!')
    else:
        form = Reservation()
    return render(request, 'reservations/planning.html', {'form': form})


def prestations(request):
    return render(request, 'reservations/prestations.html')

