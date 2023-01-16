from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def about_u(Request):
    return HttpResponse('<b>This is about us page</b>')
