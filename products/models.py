from django.db import models
from cloudinary.models import CloudinaryField

"""
QUANTITY_LIST = (
        ('100', '100'),
        ('250', '250'),
        ('500', '500'),
        ('1000', '1000'),
        ('2000', '2500'),
        ('5000', '5000'),
    )

SIZE_LIST = (
    (0, 'A5'),
    (1, 'A6'),
    (2, 'A4'),
    (3, '148mm x 148mm'),
    (3, 'DL'),

)

LAMINATE_LIST = (
    (0, 'Matt'),
    (1, 'Gloss'),
    (2, 'Soft Touch'),
)
"""

class Category(models.Model):

    #This changes the name in the admin panel from Categorys
    class Meta:
        verbose_name_plural = 'Categories' 

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):

    
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    size = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.CharField(max_length=6, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default='0.00')

    def __str__(self):
        return self.name

