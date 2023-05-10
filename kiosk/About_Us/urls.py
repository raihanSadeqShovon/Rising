from django.urls import path
from . import views

urlpatterns = [
    path('a/', views.about_u)
]