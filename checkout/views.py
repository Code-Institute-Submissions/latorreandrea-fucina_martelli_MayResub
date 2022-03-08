from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from cart.contexts import cart_contents

import stripe 
# Create your views here.
def checkout(request):
    # create payment intent 1/2
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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
    print(intent)
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KLSo1Hps3G9jcCFabV4luTBU0EI8E2yZMpVkc7Mvg54j740OKL02PLjXxS42vYxvXXFYTOn4SLNp3Pzs5GMQdU900v2uyjwKa',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)