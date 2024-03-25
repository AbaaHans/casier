
from django.contrib import admin
from django.urls import path , include
from .views import *

app_name = 'AuthGateway'
urlpatterns = [
    path('authentificate/',authentificate_user,name='connexion'),
    path('deconnexion/',deconnexion,name='deconnexion')
]
