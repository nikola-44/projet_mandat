# FERREIRA STOJKOVIC Nikola
from django.db import models

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
    statut = models.CharField()

    def __str__(self):
        if self.pour == '/':
            return self.nom
        else:
            return self.nom + ' --- ' + self.pour


class Reservation(models.Model):
    date_heure = models.DateTimeField(auto_now_add=False, null=True, blank=True)  # date par défaut aujourd'hui
    commentaire = models.TextField(blank=True, default='')
    prestations = models.ManyToManyField(Prestation, through='ResPres')

    def __str__(self):
        return 'Réservation du ' + self.date_heure.__str__()


class ResPres(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    prestation = models.ForeignKey(Prestation, on_delete=models.CASCADE)
    duree_effective = models.TimeField(blank=True, null=True)
    prix = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        unique_together = [['reservation', 'prestation']]
