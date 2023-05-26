from django.http import HttpResponse
from django.shortcuts import render
from About_Us.models import Teacher

# Create your views here.
def about_u(Request):
    return render(Request, 'about/about.html')

def teachers_info(Request):
    teach = Teacher.objects.all()
    return render(Request, 'about/t.html', {'tch' : teach})