from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse


# Create your views here.
def contact(request):
    if request.method == "POST":
        contact = Contact()
        nom = request.POST.get('nom')
        prénom = request.POST.get('prénom')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.nom = nom
        contact.prénom = prénom
        contact.email = email
        contact.message = message
        contact.save()
        return HttpResponse("<h1>Merci de nous avoir contacter !</h1>")
    return render(request, 'contact.html')
