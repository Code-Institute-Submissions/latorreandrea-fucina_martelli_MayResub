from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from .views import add_to_cart
from decimal import Decimal

def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})
    cart_items = []
    total_product = 0
    product_count = 0
    total = 0
    quantity = 0    
    
    if len(cart)>0:
        for i in cart:
            if cart[i]['material'] == 'steel':

                product = get_object_or_404(Product, pk=int(cart[str(i)]['product']))
                total += cart[i]['quantity'] * product.price
                product_count += cart[i]['quantity']
                cart_items.append({'product': product, 'quantity': cart[i]['quantity'] ,'product': product, 'material':cart[i]['material']})

            else :
                product = get_object_or_404(Product, pk=int(cart[str(i)]['product']))
                total += cart[i]['quantity'] * (product.price + 200)
                product_count += cart[i]['quantity']
                cart_items.append({'product': product, 'quantity': cart[i]['quantity'] ,'product': product, 'material':cart[i]['material']})
                print(product.price + 200)
                print(type(product.price))

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}