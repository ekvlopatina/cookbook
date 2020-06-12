from django.shortcuts import render
from django.views import generic
# Create your views here.
from catalog.models import Category, Dish

def index(request):
    num_dish = Dish.objects.count()
    context = {
    'num_dish': num_dish,
    }
    return render(request, 'index.html', context=context )

class SaladsView(generic.ListView):
    model = Dish

class DessertsView(generic.ListView):
    model = Dish

class MainCoursesView(generic.ListView):
    model = Dish
