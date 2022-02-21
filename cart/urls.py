from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
]

