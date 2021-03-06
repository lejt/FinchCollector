from django.shortcuts import render, redirect
from .models import BirdAcc, Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm

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
    birdacc = BirdAcc.objects.exclude(id__in=finch.birdacc.all().values_list('id'))
    # instantiate FeedingForm to be rendered to template
    feeding_form = FeedingForm()
    return render(
        request, 
        'finches/detail.html',
        {'finch': finch, 'feeding_form': feeding_form, 'birdacc': birdacc}
    )

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

def add_feeding(request, finch_id):
    # create instance of ModelForm using data in request.POST
    form = FeedingForm(request.POST)
    
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    
    return redirect('finches_detail', finch_id=finch_id)

class BirdAccList(ListView):
    model = BirdAcc

class BirdAccDetail(DetailView):
    model = BirdAcc

class BirdAccCreate(CreateView):
    model = BirdAcc
    fields = '__all__'

class BirdAccUpdate(UpdateView):
    model = BirdAcc
    fields = ['item', 'description']

class BirdAccDelete(DeleteView):
    model = BirdAcc
    success_url = '/birdacc/'

def assoc_birdacc(request, finch_id, birdacc_id):
    Finch.objects.get(id=finch_id).birdacc.add(birdacc_id)
    return redirect('finches_detail', finch_id=finch_id)