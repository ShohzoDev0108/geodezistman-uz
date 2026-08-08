from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kurslar/', views.kurslar_royxati, name='kurslar_royxati'),
]