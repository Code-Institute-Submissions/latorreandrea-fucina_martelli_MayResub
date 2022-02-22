from django.shortcuts import render, redirect


# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')  # taked in the product detail page
    
    cart = request.session.get('cart', {})

    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(redirect_url)