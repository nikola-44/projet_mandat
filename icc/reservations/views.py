from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def planning(request):
    return render(request, 'reservations/planning.html')


def prestations(request):
    return render(request, 'reservations/prestations.html')
