from django.shortcuts import render


# Create your views here.
def cart(request):
    """ A view to return chart page"""
    return render(request, 'cart/cart.html')