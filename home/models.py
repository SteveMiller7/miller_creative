from django.db import models
from cloudinary.models import CloudinaryField


class FeaturedPicture(models.Model):
    picture = CloudinaryField('image', default='placeholder')


class FeaturedCompany(models.Model):
    picture = models.ForeignKey('FeaturedPicture', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)


class Category(models.Model):

    #This changes the name in the admin panel from Categorys
    class Meta:
        verbose_name_plural = 'Categories' 

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):

    QUANTITY_LIST = (
        (0, '100'),
        (1, '250'),
        (2, '500'),
        (3, '1000'),
        (4, '2500'),
        (5, '5000'),
    )

    LAMINATE_LIST = (
        (0, 'Matt'),
        (1, 'Gloss'),
        (2, 'Soft Touch'),
    )

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(choices=QUANTITY_LIST)
    laminate = models.IntegerField(choices=LAMINATE_LIST)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

