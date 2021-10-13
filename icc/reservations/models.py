# FERREIRA STOJKOVIC Nikola
from datetime import date, datetime, timedelta

from django.db import models
from compte.models import Client

# Create your models here.


class Prestation(models.Model):
    LONGEUR_CHEVEUX = (
        ('Courts', 'Courts'),
        ('Longs', 'Longs'),
        ('/', '/')
    )
    STATUT = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    )
    nom = models.CharField(max_length=60)
    pour = models.CharField(max_length=6, choices=LONGEUR_CHEVEUX, default='')
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    duree = models.TimeField()
    # statut = models.CharField()

    def __str__(self):
        if self.pour == '/':
            return self.nom
        else:
            return self.nom + ' --- ' + self.pour


class Reservation(models.Model):
    date_heure = models.DateTimeField('Date-heure: JJ.MM.AAAA HH:MM (H+1)', auto_now_add=False, null=True, blank=True)  # date par défaut aujourd'hui
    commentaire = models.TextField(blank=True, default='')
    prestations = models.ManyToManyField(Prestation, through='ResPres')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Réservation du ' + self.date_heure.__str__()

    def is_past_due(self):
        return datetime.now().date() > self.date_heure.date()

    def heure_fin(self):
        hf = self.date_heure
        if self.prestations.all():
            for prestation in self.prestations.all():
                hf = self.date_heure - timedelta(hours=prestation.duree.hour, minutes=prestation.duree.minute)
            return hf
        else:
            return self.date_heure.time()


class ResPres(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    prestation = models.ForeignKey(Prestation, on_delete=models.CASCADE)
    duree_effective = models.TimeField(blank=True, null=True, default='prestation.duree')
    prix = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = [['reservation', 'prestation']]
