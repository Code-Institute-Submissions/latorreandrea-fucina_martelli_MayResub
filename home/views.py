from django.shortcuts import render
from products.models import Product, Category


# Create your views here.
def index(request):
    """ A view to render homepage """
    return render(request, "home/index.html")


def payment_secure(request):
    """ A view to render payment info page """
    return render(request, "home/payment.html")


def shipping(request):
    """ A view to render shipment info page """
    return render(request, "home/shipping.html")


def privacy(request):
    """ A view to render privacy info page """
    return render(request, "home/privacy.html")
