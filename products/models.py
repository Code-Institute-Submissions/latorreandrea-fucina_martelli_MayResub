from django.db import models


# Create your models here.

DISCOUNT = (
    ("0", "no"),
    ("10", "10% discount"),
    ("20", "20% discount"),
    )

MATERIAL = (
    ('steel', 'steel'),
    ('titanium', 'titanium'),   
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
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    discount = models.CharField(max_length=100,
                  choices=DISCOUNT, default=1)
    material = models.CharField(max_length=100,
                  choices=MATERIAL, default=0)

    def __str__(self):
        return self.name