from django.shortcuts import render
from .models import Newsletter
from .forms import NewsletterSignUpForm
from django.contrib import messages
# Create your views here.


def newsletter_signup(request):
    '''view for register a user for our newsletter'''
    form = NewsletterSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Newsletter.objects.filter(email=instance.email).exists():
            messages.error(request, 'sorry this email already exist')
            return render(request, "newsletter/sign_up.html")
        else:            
            instance.save()
            messages.success(request, 'your email is now registered!')

    context = {
        'form': form,
    }
    template = "newsletter/sign_up.html"
    return render(request, template, context)


def newsletter_unsubscribe(request):
    '''view for unsubscribe a user from our newsletter'''
    form = NewsletterSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Newsletter.objects.filter(email=instance.email).exists():
            Newsletter.objects.filter(email=instance.email).delete()
            messages.success(request, 'you are no longer registered to the newsletter')
        else:
            messages.error(request, "sorry this email doesn't exists")
            return render(request, "newsletter/unsubscribe.html")

    context = {
        'form': form,
    }

    template = "newsletter/unsubscribe.html"
    return render(request, template, context)