from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def deep_learning(request):
    return HttpResponse("This is Deep learning app not machine learning method")