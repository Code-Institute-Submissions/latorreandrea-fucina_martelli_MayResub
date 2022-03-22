from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from .models import Product, Category, ProductReview
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from accounts.models import Account
from .forms import ProductForm
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

    paginator = Paginator(products, 6) # Show 6 products per page.
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'products': products,
        'search': query,
        
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show detail and reviews of selected product"""
    product = get_object_or_404(Product, pk=product_id)  
    reviews = ProductReview.objects.filter(product=product_id)

    #paginating (https://docs.djangoproject.com/en/4.0/topics/pagination/)
    paginator = Paginator(reviews, 10) # Show 10 reviews per page.
    page_number = request.GET.get('page')
    page_reviews = paginator.get_page(page_number)


    context = {
        'product': product,
        'page_reviews': page_reviews,
    }

    return render(request, 'products/product_detail.html', context)


def product_review(request, product_id):
    """ A view to review the selected product """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_review.html', context)


def add_review(request, product_id):
    """
    View to add review
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        if request.method == 'POST':
            stars = request.POST.get('stars')
            content = request.POST.get('content')
            user = request.user
            account = Account.objects.get(user=request.user)
            review = ProductReview.objects.create(product=product, user=user, stars=stars, content=content, account=account)            
            messages.success(request, f"Your review of {product.name} has been added")
            return redirect('product_detail', product_id=product_id)


def add_product(request):
    """
    add product in store
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added in the store')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'check that you have filled in the form correctly')

    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def delete_product(request, product_id):
    """delete selected product"""
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('products'))
    

def edit_product(request, product_id):
    """edit selected product"""
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'you have edit {product.name}')
            return redirect('product_detail', product_id=product_id)
        else:
            messages.error(request, 'an error was encountered')
    else:
        form = ProductForm(instance=product)      
    
    template = 'products/edit_product.html'
    context = {
        'product': product,
        'form': form,
    }
    return render(request, template, context)


