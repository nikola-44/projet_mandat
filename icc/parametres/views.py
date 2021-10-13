# Nikola Stojkovic Dorian Châtelain
from django.shortcuts import render, redirect

# Create your views here.
from .forms import SalonForm
from .models import Parametres



def gererSalon(request):
    parametres = Parametres.objects.all()
    return render(request, '../templates/gererSalon.html', {'parametres': parametres})


def modifier_salon(request, pk):
    if request.method == 'POST':
        pi = Parametres.objects.get(id=pk)
        fm = SalonForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/parametres/gererSalon')
    else:
        pi = Parametres.objects.get(id=pk)
        fm = SalonForm(instance=pi)
    return render(request, '../templates/modifier_salon.html', {'form': fm})

