from django.urls import path
from . import views

urlpatterns = [
    path('b/', views.blogs1),
    path('f/', views.showformdata),
]