from django.contrib import admin
from .models import Product # importing Products from models.py
# Register your models here.
admin.site.register(Product)