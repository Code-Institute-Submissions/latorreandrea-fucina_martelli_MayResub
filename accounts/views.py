from django.shortcuts import render, get_object_or_404
from .models import Account
from checkout.models import Order
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def accounts(request):
    """ A view to show to the user the order history and manage his account"""
    account = get_object_or_404(Account, user=request.user)
    
    context = {
        'account': account
    }   
    return render(request, 'accounts/accounts.html', context)


@login_required
def order_history(request):
    """ A view to show the order history"""
    account = get_object_or_404(Account, user=request.user)
    orders = Order.objects.filter(account=account)   
    
    context = {
       'accounts_orders_list': orders
    }   
    return render(request, 'accounts/orderhistory.html', context)

