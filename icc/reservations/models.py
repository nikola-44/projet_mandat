from django.db import models
from datetime import datetime, date

# Create your models here.


class Reservation(models.Model):
    commentaire = models.TextField(blank=True, default='')
    date = models.CharField(max_length=255)
    heure = models.TimeField()
