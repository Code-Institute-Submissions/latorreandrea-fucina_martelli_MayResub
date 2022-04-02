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
            print("sorry this email already exist")
        else:
            instance.save()

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
        if Newsletter.objects.filter(email=instance.email).exist():
            NewsletterUser.objects.filter(email=instance.email).delete()
        else:
            print("sorry this email doesn't exist")

    context = {
        'form': form,
    }

    template = "newsletter/unsubscribe.html"
    return render(request, template, context)