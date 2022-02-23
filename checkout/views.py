from django.shortcuts import render


# Create your views here.
def checkout(request):
    cart = request.session.get('cart', {})
    # preveent perople accessin manually the Url
    if not cart:
        messages.error(request, "there's nothing in your cart!")   
        return redirect(reverse('products'))
    