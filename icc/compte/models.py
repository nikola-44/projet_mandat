# Châtelain Dorian
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    dateNaissance = models.DateField()
    telephone = models.CharField(max_length=12)
    genre = models.CharField(max_length=15)


def __str__(self):
    return self.nom
