from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def blogs1(request):
    return render(request, 'blogs.html')
    