from django.urls import path

from . import views

urlpatterns = [
    path('', views.materiallar_royxati, name='materiallar_royxati'),
]
