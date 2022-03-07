from django import forms
from .models import Order, OrderLineItem
from products.models import Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'email_address', 'phone_number', 'town_or_city',
            'street_address1', 'street_address2',
            'country', 'county', 'postcode')
    
    def __int__(self, *args, **kwargs):
        '''add placeholders, set autofocus for form order'''

        super(). __int__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name', 
            'email_address': 'email@email.example', 
            'phone_number': 'Phone Number', 
            'town_or_city': 'City', 
            'street_address1': 'main Street Adress', 
            'street_address2': 'secondary Street Adress',
            'country': 'Country', 
            'county': 'County/Region',
            'postcode': 'Postal Code',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = f'{placeholders[field]}'
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'
        self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].label = False



class OrderStatus(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_status', )