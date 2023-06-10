from django.http import HttpResponse
from django.shortcuts import render
from . forms import TeachersRegistration

# Create your views here.
def blogs1(request):
    return render(request, 'blogs/blogs.html')
    

def showformdata(request):
    fm = TeachersRegistration()
    fm.order_fields(field_order=['email','first_name','last_name'])
    return render(request, 'blogs/forms.html', {'form': fm})