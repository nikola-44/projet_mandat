# Generated by Django 3.2.6 on 2021-10-18 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0009_auto_20211018_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prix_achat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='produit',
            name='prix_vente',
            field=models.IntegerField(default=0),
        ),
    ]
