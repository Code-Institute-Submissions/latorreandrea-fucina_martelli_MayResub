from django.db import models
from django.contrib.auth.models import User


# Create your models here.

DISCOUNT = (
    ("0", "no"),
    ("10", "10% discount"),
    ("20", "20% discount"),
    )



class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)    
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    discount = models.CharField(max_length=100,
                  choices=DISCOUNT, default=1)
    material = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_rating(self):
        """function to get average review"""
        total = sum(int(review['stars']) for review in self.reviews.values())

        return total / self.reviews.count()


class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()

    
