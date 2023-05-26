from django.urls import path
from . import views

urlpatterns = [
    path('a/', views.about_u),
    path('t/' , views.teachers_info),
]