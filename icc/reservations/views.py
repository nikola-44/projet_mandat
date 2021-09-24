from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Reservation
# Create your views here.


# @login_required(login_url='acces')
def planning(request):
    return render(request, 'reservations/planning.html')


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

