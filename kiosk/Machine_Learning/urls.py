from django.urls import path
from . import views

urlpatterns = [
    path('', views.machine),
    path('dl/', views.deep_learning),
    path('about_us/', views.about_us)
]