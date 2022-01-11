from django.shortcuts import render
from django.http import HttpResponse

from .models import finches as finches

# Create your views here.
def home(request):
    return HttpResponse('<h1>hi</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches':finches})