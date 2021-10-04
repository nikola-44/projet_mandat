# FERREIRA STOJKOVIC Nikola
from django.urls import path
from . import views

appname = 'reservations'


urlpatterns = [
    path('planning-visiteurs/', views.planning_visiteurs, name='planning-visiteurs'),
    path('planning-clients/', views.planning_clients, name='planning-clients'),
    path('planning-mandante', views.planning_mandante, name='planning-mandante'),

    path('rendezvous/', views.rendezvous, name='rendezvous'),

    path('prestations/', views.prestations, name='prestations'),
    # path('reserver/', views.reserver, name='reserver'),
    # path('test-<int:jour>/', views.test, name='test'),
    path('test-prestations/', views.test_prestations, name='test-prestation'),
    # path('<int:jour>/', views.test, name='test-jour')

]
