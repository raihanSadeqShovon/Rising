from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine(request):
    return render(request, 'machine_learning.html')
