from django.urls import path

from . import views

urlpatterns = [
    path('', views.uskunalar_royxati, name='uskunalar_royxati'),
]
