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
    cart = request.session.get('cart', {})
    request.session['material'] = request.POST.get('material')
    
    data = {}
    data['product'] = id
    data['material'] = request.POST.get('material')
    data['quantity'] = quantity

    element_to_add = False
    if len(cart)>0: 
        for k,v in cart.items():
            if data['product'] == v['product'] and data['material'] == v['material']:
                tot = quantity + v['quantity']
                data['quantity'] = tot
                cart[k].update(data)
                break
            else:
                if int(k)>=len(cart):
                    element_to_add = True
    else:
        cart[1] = data

    if element_to_add:
        cart[len(cart)+1] = data

    

    request.session['cart'] = cart
    redirect_url = request.POST.get('redirect_url')  # taked in the product detail page

    return redirect(redirect_url)


def amend_cart(request, id, material):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    product = Product.objects.get(pk=id)

    data = {}

    for k,v in cart.items():
        if v['product'] == str(id) and v['material'] == material:
            data['product'] = cart[k]['product']
            data['material'] = cart[k]['material']
            data['quantity'] = quantity

            cart[k] = data

    request.session['cart'] = cart
    messages.success(request, f"Updated {product.name} to your bag")
    return redirect(reverse('view_cart'))


def remove_item(request, id, material):
    """
    Remove the specified product from the cart
    """
    product = Product.objects.get(pk=id)

    cart = request.session.get('cart', {})
    index_to_remove = None

    for k,v in cart.items():
        if v['product'] == str(id) and v['material'] == material:
            index_to_remove = k
    
    if index_to_remove != None:
        cart.pop(index_to_remove)

    request.session['cart'] = cart
    messages.success(request, f"Removed {product.name} from your bag")
    return redirect(reverse('view_cart'))



