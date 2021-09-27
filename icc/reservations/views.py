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
    return render(request, 'reservations/test-prestations.html', {'prestations': prestations})


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

