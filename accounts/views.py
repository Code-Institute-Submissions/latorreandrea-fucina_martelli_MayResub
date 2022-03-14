from django.shortcuts import render, get_object_or_404
from .models import Account
from checkout.models import Order

# Create your views here.
def accounts(request):
    """ A view to show to the user the order history and manage his account"""    
    return render(request, 'accounts/accounts.html')

def order_history(request):
    """ A view to render a list of the orders of the user"""
    user = request.user
    user_id = get_object_or_404(Account, username=user)
    orders = order.objects.filter(name=user_id)
    context = {

    }
    
    return render(request, 'reservations.html', context)