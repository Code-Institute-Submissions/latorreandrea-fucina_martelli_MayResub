from django import forms
from .models import Order, OrderLineItem
from products.models import Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'email_address', 'phone_number', 'town_or_city', 'street_address1', 'street_address2',
            'country', 'county', 'postcode')


class OrderStatus(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_status', )