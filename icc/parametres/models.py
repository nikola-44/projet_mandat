# Dorian Châtelain

from django.db import models


# Create your models here.

class Parametres(models.Model):
    stockMinPVente = models.IntegerField()
    prixLivraison = models.IntegerField()
    telephone = models.IntegerField()
    adresse = models.CharField(max_length=15)
    nomSalon = models.CharField(max_length=150)

    def __str__(self):
        return self.nomSalon
