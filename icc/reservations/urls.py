from django.urls import path
from . import views

appname = 'reservations'


urlpatterns = [
    path('', views.planning, name='planning'),
    path('prestations/', views.prestations, name='prestations'),
    path('reserver/', views.reserver, name='reserver'),
    path('test/', views.test, name='test'),
    path('test-prestations/', views.test_prestations, name='test-prestation'),

]
