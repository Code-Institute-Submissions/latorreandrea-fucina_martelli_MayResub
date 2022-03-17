from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Product, Category
# Create your views here.


def all_products(request):
    """ A view to show products / searched products /selected category"""
    products = Product.objects.all()
    query = None
    category = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
        if 'category' in request.GET:
            category = request.GET['category']           
            products = products.filter(category__name=category)
            
            

    context = {
        'products': products,
        'search': query,
        'category_selected': category,
    }
    return render(request, 'products/products.html', context)



def product_detail(request, product_id):
    """ A view to show detail of selected product"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def product_review(request, product_id):
    """ A view to show detail of selected product"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_review.html', context)


def add_review(request, product_id):
    """
    Take review and create a rating for a product
    """
    print(request.POST.get('review'))
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)