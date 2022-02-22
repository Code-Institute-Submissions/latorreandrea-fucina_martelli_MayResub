from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<id>/', views.add_to_cart, name='add_to_cart'),
]

