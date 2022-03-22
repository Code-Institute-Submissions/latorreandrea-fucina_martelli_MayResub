from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['material', 'sku']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        for category in categories:
            category.id = category.get_friendly_name()
        