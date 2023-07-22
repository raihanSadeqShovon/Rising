from  django.urls import path
from . import views

urlpatterns = [
    path('deepl/', views.deep_learning, name='dl'),
    path('register/', views.registration),
]
