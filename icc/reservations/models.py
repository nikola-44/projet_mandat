from django.db import models
from datetime import datetime, date

# Create your models here.


class Reservation(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    commentaire = models.TextField(blank=True, default='')

    def __str__(self):
        return 'Réservation du ' + self.date.strftime('%d.%m.%Y') + ' - ' + self.heure.__str__()


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
