from django.db import models
from django.contrib import admin

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    ram = models.IntegerField()
    memory = models.FloatField()
    photo = models.ImageField(upload_to='photos/')
    
class   Productlist(admin.ModelAdmin):
    list_display = ('name', 'ram', 'memory')

class  People(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/')
    
class Peoplelist(admin.ModelAdmin):
    list_display = ('name', 'designation',)