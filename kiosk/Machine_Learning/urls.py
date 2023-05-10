from django.urls import path
from . import views

urlpatterns = [
    path('mac/', views.machine, name='mac'),
    path('rn/', views.random, name='antactn'),
    path('dt/', views.dt),
    path('knn/', views.knn),     
]