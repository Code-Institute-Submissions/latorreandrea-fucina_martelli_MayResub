from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):
    cart = request.session.get('cart', {})
    # preveent perople accessin manually the Url
    if not cart:
        messages.error(request, "there's nothing in your cart!")   
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KLSo1Hps3G9jcCFabV4luTBU0EI8E2yZMpVkc7Mvg54j740OKL02PLjXxS42vYxvXXFYTOn4SLNp3Pzs5GMQdU900v2uyjwKa',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)