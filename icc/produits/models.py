from django.db import models


# Create your models here.

class Produit(models.Model):
    nom = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    # image = models.ImageField()
    capacite = models.IntegerField()
    statut = models.CharField(max_length=250)

    def __str__(self):
        return self.nom
