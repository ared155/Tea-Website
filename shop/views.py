from unicodedata import category
from urllib import response
from django.shortcuts import render
from .models import Categories, Products
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def categories_list(request):
    categories=Categories.objects.all()
    return render(request, 'shop/categories.html',{'categories':categories})


def product(request,title):
    products=Products.objects.filter(category=title)
    return render(request, 'shop/product_list.html',{'products':products})

def product_detail(request, title, slug):
    # return HttpResponse()
    product=get_object_or_404(Products, slug=slug, 
                            title=title)
    # product=Products.objects.get(slug=slug)
    return render(request, 'shop/product_detail.html',{'product':product})
    

