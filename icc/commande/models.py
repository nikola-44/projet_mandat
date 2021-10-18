from django.db import models
from compte.models import Client
from produits.models import Produit


# Create your models here.


class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    statut_commande = models.CharField(max_length=200, null=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class CommandeItem(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, blank=True, null=True)
    commande = models.ForeignKey(Commande, on_delete=models.SET_NULL, blank=True, null=True)
    quantite = models.IntegerField(default=0, null=True, blank=True)
    date_ajoute = models.DateTimeField(auto_now_add=True)


class AdresseCommande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    commande = models.ForeignKey(Commande, on_delete=models.SET_NULL, blank=True, null=True)
    adresse = models.CharField(max_length=200, null=True)
    ville = models.CharField(max_length=200, null=True)
    pays = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_ajouter = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.adresse
