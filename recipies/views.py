from django.shortcuts import render
from .models import Recipes
from django.http import HttpResponse
# Create your views here.

def recipe_list(request):
    recipes=Recipes.objects.all().order_by('date')
    return render(request, 'recipies/recipe_list.html',{'recipes':recipes})

def recipe_detail(request, slug):
    # return HttpResponse()
    recipe=Recipes.objects.get(slug=slug)
    return render(request, 'recipies/recipe_detail.html',{'recipe':recipe})