from django.contrib import admin
from .models import Product, Category, ProductReview


# customizing admin info displayed for products
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
    )
    ordering = ('name',)
    search_fields = ['name', 'category__name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    ordering = ('name',)
    search_fields = ['name']


# Register models for products to keep update the catalougue from admin panel
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview)
