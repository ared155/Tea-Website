from email.quoprimime import body_check
from pyexpat import model
from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.
class Categories(models.Model):
    title=models.CharField(max_length=100, primary_key=True, unique=True, blank=False)
    slug=models.SlugField()
    body=models.TextField()
    thumb=models.ImageField(blank=True)
    def __str__(self):
        return self.title



class Products(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    price=models.IntegerField()
    thumb=models.ImageField()
    category=models.ForeignKey(Categories, models.SET_NULL, blank=True, null=True, to_field='title')
    # objects = models.Manager()
    def __str__(self):
        return self.title  
    # class Meta:
    #     db_table='products'
