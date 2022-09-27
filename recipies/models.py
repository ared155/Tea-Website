from datetime import date
from email.base64mime import body_encode
from logging.handlers import SYSLOG_UDP_PORT
from pickle import TRUE
from turtle import title
from django.db import models

# Create your models here.
class Recipes(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    description=models.TextField(max_length=200,default="Some String")
    body=models.TextField()
    date=models.DateField(auto_now_add=True)
    thumb=models.ImageField(blank=True)

    def __str__(self):
        return self.title

# def snippet(self):
#     return self.body[:20]+'...'