from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')  # taked in the product detail page    
    cart = request.session.get('cart', {})
    product = Product.objects.get(pk=id)

    if id in cart:
        cart[id] = int(cart[id]) + quantity
        messages.success(request, f"Updated {product.name} to your bag")
    else:
        cart[id] = cart.get(id, quantity)
        messages.success(request, f"Added {product.name} to your bag")
# prevent users order more than 10 piece
    
    if cart[id] < 11:
        request.session['cart'] = cart
    else:
        messages.error(request, f"You can't order more than 10 piece")
        return render(request, 'home/500.html')       
    
    return redirect(redirect_url)
    

def amend_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    product = Product.objects.get(pk=id)


    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    messages.success(request, f"Updated {product.name} to your bag")
    return redirect(reverse('view_cart'))


def remove_item(request, id):
    """
    Remove the specified product from the cart
    """
    product = Product.objects.get(pk=id)

    cart = request.session.get('cart', {})

    cart.pop(id)

    request.session['cart'] = cart
    messages.success(request, f"Removed {product.name} from your bag")
    return redirect(reverse('view_cart'))