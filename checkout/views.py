from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from cart.contexts import cart_contents
from .models import Order, OrderLineItem
from products.models import Product


import stripe 
# Create your views here.
def checkout(request):
    # create payment intent 1/2
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name':request.POST['full_name'],
            'email_address':request.POST['email_address'],
            'phone_number':request.POST['phone_number'],
            'town_or_city':request.POST['town_or_city'],
            'street_address1':request.POST['street_address1'],
            'street_address2':request.POST['street_address2'],
            'country':request.POST['country'],
            'county':request.POST['county'],
            'postcode':request.POST['postcode'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()            
            for i in cart:
                product = get_object_or_404(Product, pk=int(cart[str(i)]['product']))
                order_line_item = OrderLineItem(   
                    order=order,                 
                    product=product,
                    quantity=cart[i]['quantity'],
                    material=cart[i]['material'],                    
                )
                print(order_line_item)
                order_line_item.save()
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('success', args=[order.order_number]))
        else:
            messages.error(request, 'errors in the form')

    else:
        cart = request.session.get('cart', {})
        # preveent perople accessin manually the Url
        if not cart:
            messages.error(request, "there's nothing in your cart")   
            return redirect(reverse('products'))
        
        current_cart = cart_contents(request)
        total = current_cart['total']

        # create payment intent 2/2
        stripe_total = round(total*100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        )
        
        order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def success(request, order_number):
    '''.
    View to render success page for payments
    '''
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order {order_number} Sended, a confermation email will be sent to {order.email_address}')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/success.html'
    context = {
        'order' : order,
    }

    return render(request, template)