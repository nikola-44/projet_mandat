from django.db import models
from datetime import datetime, date

# Create your models here.


class Reservation(models.Model):
    date = models.DateField()
    heure = models.TimeField()
    commentaire = models.TextField(blank=True, default='')

    def __str__(self):
        return self.commentaire
