# Zumeri Faton et Châtelain Dorian
from django.db import models


# Create your models here.

class Produit(models.Model):
    nom = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    categorie = models.CharField(max_length=250)
    image = models.ImageField()
    capacite = models.IntegerField()
    prix_achat = models.IntegerField()
    prix_vente = models.IntegerField()
    statut = models.CharField(max_length=250)
    quantite = models.IntegerField()

    def __str__(self):
        return self.nom
