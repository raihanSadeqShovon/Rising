from django.urls import path
from . import views

urlpatterns = [
    path('func/', views.data_analysis, name='data'),
    path('class/', views.Data_analysis.as_view()),
]