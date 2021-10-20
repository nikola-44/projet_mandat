# Zumeri Faton
from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
from django.core.mail import send_mail


# Create your views here.
from django.conf import settings


def contact(request):
    if request.method == "POST":
        nom = request.POST['nom']
        mail = request.POST['email']
        message = request.POST['message']
        send_mail(
            nom,
            message,
            mail,
            [settings.EMAIL_HOST_USER],
            fail_silently = False
        )
        # contact.save()
        # form = request.POST
        # Contact.objects.create(
        #     nom=form['nom'],
        #     # prenom=form['prenom'],
        #     email=form['email'],
        #     message=form['message'],
        # )
        # send_mail(
        #     form['nom'],
        #     form['message'] + '\n from \n' + form['email'],
        #     settings.EMAIL_HOST_USER,
        #     # [form['email']],
        #     ['faton.zmr@eduge.ch'],
        #
        # )
        #
        # contact.save()
        return HttpResponse("<h1>Merci de nous avoir contacter !</h1>")
    return render(request, 'contact.html')
