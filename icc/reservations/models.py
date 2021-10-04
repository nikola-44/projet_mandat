# FERREIRA STOJKOVIC Nikola
import time

from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime, date

# Create your models here.
import manage


class Prestation(models.Model):

    LONGEUR_CHEVEUX = (
        ('Courts', 'Courts'),
        ('Longs', 'Longs'),
        ('/', '/')
    )

    nom = models.CharField(max_length=60)
    pour = models.CharField(max_length=6, choices=LONGEUR_CHEVEUX, default='')
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    duree = models.TimeField()

    def __str__(self):
        return self.nom + ' ' + self.pour + ' - ' + self.duree.__str__() + ' - ' + self.prix.__str__()


class Reservation(models.Model):
    date_heure = models.DateTimeField(auto_now_add=False, null=True, blank=True)  # date par défaut aujourd'hui
    commentaire = models.TextField(blank=True, default='')
    # prestations = models.ManyToManyField(Prestation, related_name='prestations')

    def __str__(self):
        return 'Réservation du ' + self.date_heure.__str__()

    # def heure_fin(self):
    #     heures_prestation = 0
    #     minutes_prestation = 0
    #     for p in self.prestations.all():
    #         heures_prestation += p.duree.hour
    #         minutes_prestation += p.duree.minute
    #
    #     calcul_heures, calcul_minutes = divmod(minutes_prestation / 60, 1)
    #     calcul_minutes = calcul_minutes * 60
    #
    #     heure_fin = self.heure.hour + int(calcul_heures)
    #     minute_fin = self.heure.minute + int(calcul_minutes)
    #
    #     r_heure, r_minute = divmod((self.heure.minute + int(calcul_minutes)) / 60, 1)
    #     r_minute = r_minute * 60
    #     r_heure = heure_fin + r_heure
    #
    #     if r_heure < 10:
    #         r_heure = '0' + str(round(r_heure))
    #     else:
    #         r_heure = str(round(r_heure))
    #
    #     if r_minute < 10:
    #         r_minute = '0' + str(round(r_minute))
    #     else:
    #         r_minute = str(round(r_minute))
    #
    #     reservation_heure_fin = str(r_heure) + ':' + str(r_minute)
    #     return reservation_heure_fin

    # def prix_total(self):
    #     total = 0
    #     for prestation in self.prestations.all():
    #         total += prestation.prix
    #     return total
    #
    # def liste_prestations(self):
    #     liste = []
    #     for prestation in self.prestations.all():
    #         liste.append(prestation.nom)
    #     return liste
