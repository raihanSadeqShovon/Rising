from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def data_analtysis(request):
    return HttpResponse("<p>This is data analysis app</p>")