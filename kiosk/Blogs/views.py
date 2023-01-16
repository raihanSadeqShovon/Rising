from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blogs1(request):
    return HttpResponse('<p><b>This is first blog function</b></p>')
    