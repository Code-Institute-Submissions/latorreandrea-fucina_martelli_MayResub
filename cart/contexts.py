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
            product = get_object_or_404(Product, pk=int(cart[str(i)]['product']))
            total += cart[i]['quantity'] * product.price
            product_count += cart[i]['quantity']
            cart_items.append({'product': product, 'quantity': cart[i]['quantity'] ,'product': product, 'material':cart[i]['material']})

    # print(cart_items)
    ''' for id, quantity in cart.items(): 
        product = get_object_or_404(Product, pk=int(id))
        print(product)

        if 'material' in request.session:
            product.material = request.session['material']
            print(product.material)
            total += quantity * product.price
            product_count += quantity
            cart_items.append({'id': id, 'quantity': quantity,'product': product, 'material':product.material}) '''

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}