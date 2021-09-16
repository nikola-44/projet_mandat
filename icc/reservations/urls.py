from django.urls import path
from . import views

appname = 'reservations'


urlpatterns = [
    path('', views.planning, name='planning'),
]
