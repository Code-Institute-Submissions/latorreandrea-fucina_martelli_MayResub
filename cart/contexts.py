from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


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
    

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total_product += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity,
                           'product': product})
        


    return {'cart_items': cart_items, 'total': total, 'total_product': total_product, 'product_count': product_count}