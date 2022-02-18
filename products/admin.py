from django.contrib import admin
from .models import Product, Category

# Register models for products to keep update the catalougue from admin panel
admin.site.register(Product)
admin.site.register(Category)