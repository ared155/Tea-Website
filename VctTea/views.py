# from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('HOMEPAGE')
    return render(request, 'home.html')

# def recipies(request):
#     return HttpResponse('RECIPIES')
#     return render(request, 'recipies.html')
