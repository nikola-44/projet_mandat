from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required(login_url='acces')
def planning(request):
    return render(request, 'reservations/planning.html')
