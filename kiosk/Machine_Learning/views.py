from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def machine(request):
    Teachers = {'names' : ['Raihan', 'Sadeq', 'Shovon']}
    return render(request, 'machine_learning/machine_learning.html', context=Teachers)

def random(request):
    return render(request, 'machine_learning/random_forest.html')

def dt(request):
    return render(request, 'machine_learning/DT.html')

def knn(request):
    return render(request, 'machine_learning/knn.html')

