# Generated by Django 3.2.6 on 2021-10-19 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_alter_reservation_date_heure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respres',
            name='duree_effective',
            field=models.TimeField(blank=True, default='00:00', null=True),
        ),
    ]
