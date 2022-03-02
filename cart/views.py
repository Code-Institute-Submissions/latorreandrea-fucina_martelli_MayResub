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
    material = request.POST.get('material')
    data = {"product": id, "material": material, "quantity": quantity}
    request.session["cart"] = cart
    
    if id in cart:
        if cart[id]['quantity'] < 11: # prevent users order more than 10 piece
            data_material = data['material'] 
            stored_material = cart[id]['material']
            if data_material == stored_material:
                add_qty = data['quantity']
                cart[id]['quantity'] += add_qty
                messages.success(request, f"Updated {product.name} to your bag")
            else:            
                cart[id] = cart.get(id, data)
                print(cart)
                messages.error(request, f"You already have {product.name} in the cart of another material. For logistical reasons we cannot sell the same product in different materials in the same order")
        else:
            messages.error(request, f"You can't order more than 10 piece")
            return render(request, 'home/500.html')

    else:
        cart[id] = cart.get(id, data)
        messages.success(request, f"Added {product.name} to your bag")

    return redirect(redirect_url)


'''    
    if cart[id]['quantity'] < 11:
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

    cart[id]['quantity'] = int(quantity)


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
'''