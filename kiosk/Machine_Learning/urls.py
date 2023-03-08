from django.urls import path
from . import views

urlpatterns = [
    path('mac/', views.machine),
    path('rn/', views.random),
    path('dt/', views.dt),
    path('knn/', views.knn),
    
]