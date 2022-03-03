from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<id>/', views.add_to_cart, name='add_to_cart'),
    path('amend/<id>/<str:material>/', views.amend_cart, name='amend_cart'),
    path('remove/<id>/<str:material>/', views.remove_item, name='remove_item'),
]
