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

    for id, data in cart.items():
        product = get_object_or_404(Product, pk=int(id))
        total += data['quantity'] * product.price
        product_count += data['quantity']
        cart_items.append(data)
    
    print(cart)
    print('siamo nel cart')
        
    
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
