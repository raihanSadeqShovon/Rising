from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine(request):
    return HttpResponse("<h1>Welcome to machine learning app</h1>")

def deep_learning(request):
    return HttpResponse("Welcome to deep learning app")

def about_us(request):
    return HttpResponse("Welcome to About us app inside machine learning app")
