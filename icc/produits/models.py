# Zumeri Faton et Châtelain Dorian
from django.db import models


# Create your models here.

class Produit(models.Model):
    Categorie_prod = (
        ('Colorés', 'Colorés'),
        ('Permanantés', 'Permanantés'),
        ('Endommagés', 'Endommagés'),
        ('Fins Affaiblis', 'Fins Affaiblis'),
        ('Normaux sains', 'Normaux sains'),
        ('White Silver', 'White Silver'),
        ('Cocoa Brown', 'Cocoa Brown'),
        ('Coral Red', 'Coral Red'),
        ('Saffron Copper', 'Saffron Copper'),
        ('Violet Lavender', 'Violet Lavender'),
        ('Cheveux Stressés', 'Cheveux Stressés'),
        ('En profondeur', 'En profondeur')
    )

    Type_choix = (
        ('Shampoo', 'Shampoo'),
        ('Conditioner', 'Conditioner'),
        ('Treatment', 'Treatment'),
        ('Travel Pack', 'Travel Pack'),
        ('Protector', 'Protector'),
        ('Cream', 'Cream'),
        ('Drops', 'Drops'),
        ('Balm', 'Balm'),
        ('Mist', 'Mist'),
        ('Hydra Oil', 'Hydra Oil'),
        ('Oil', 'Oil'),
        ('Mask', 'Mask'),
        ('Serum', 'Serum'),
    )

    nom = models.CharField(max_length=250)
    type = models.CharField(max_length=250, choices=Type_choix, default='')
    categorie = models.CharField(max_length=250, choices=Categorie_prod, default='')
    image = models.ImageField()
    capacite = models.PositiveIntegerField()
    prix_achat = models.PositiveIntegerField()
    prix_vente = models.PositiveIntegerField()
    statut = models.CharField(max_length=250)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return self.nom
