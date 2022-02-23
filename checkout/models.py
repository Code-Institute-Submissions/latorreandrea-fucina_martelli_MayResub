import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product

ORDER_STATUS = (
    ('Order Received', 'Order Received'),
    ('Delivered', 'Delivered'),
)

# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    email_address = models.CharField(max_length=100, blank=False, default="")
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField(auto_now_add=True)
    order_status = models.CharField(
        choices=ORDER_STATUS, max_length=50, default='Order Received', blank=True)
    total = models.DecimalField(
        blank=False, default=0, max_digits=4, decimal_places=2)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, related_name='lineitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(blank=False)
    total = models.DecimalField(
        blank=False, default=0, max_digits=6, decimal_places=2)

    def save(self, *args, **kwargs):
        """
        Save method to set lineitem total
        """
        
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'

    
