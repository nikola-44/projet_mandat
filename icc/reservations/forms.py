# FERREIRA STOJKOVIC Nikola

from django.forms import ModelForm
from .models import Reservation, Prestation


# class Rendezvous(forms.ModelForm):
#     # date = forms.DateField()
#     # heure = forms.TimeField()
#     # commentaire = forms.CharField(widget=forms.Textarea())
#
#     class Meta:
#         model = models.Reservation
#         fields = ['date_heure', 'commentaire']


class PrestationForm(ModelForm):
    class Meta:
        model = Prestation
        fields = '__all__'
