from django import forms
from .models import Newsletter


class NewsletterSignUpForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
