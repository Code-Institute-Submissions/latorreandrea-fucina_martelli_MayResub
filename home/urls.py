
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('payment-card-security/', views.payment_secure, name='payment_secure'),
    path('shipping-and-payment/', views.shipping, name='shipping'),
    path('privacy/', views.privacy, name='privacy')

]
