from django.contrib import admin
from .models import Product,Productlist
from .models import People,Peoplelist

# Register your models here.

admin.site.register(Product,Productlist)
admin.site.register(People,Peoplelist)