from django.shortcuts import render, get_object_or_404
from .models import Account
from checkout.models import Order


# Create your views here.
def accounts(request):
    """ A view to show to the user the order history and manage his account"""    
    return render(request, 'accounts/accounts.html')

def shipment_info(request, account):
    """ A view to show detail of selected product"""
    account = get_object_or_404(Account, pk=product_id)
    context = {
    }
    return render(request, 'accounts/shipmentinfo.html', context)


def order_history(request):
    """ A view to render a list of the orders of the user"""
    user = request.user
    print(user)    
    orders = Order.objects.filter(account=user.id)
    context = {
        'orders': orders
    }
    
    return render(request, 'accounts/orderhistory.html', context)