from django.shortcuts import render, redirect
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

    # instantiate FeedingForm to be rendered to template
    feeding_form = FeedingForm()
    return render(
        request, 
        'finches/detail.html',
        {'finch': finch, 'feeding_form': feeding_form}
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
