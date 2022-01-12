from django.shortcuts import render
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# from .models import finches as finches
from main_app.models import Finch

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches':finches})

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})

# class based views below:
class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'family', 'description', 'fav_food', 'weight']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'description', 'fav_food']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

