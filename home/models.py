from django.db import models
from cloudinary.models import CloudinaryField


class FeaturedPicture(models.Model):
    picture = CloudinaryField('image', default='placeholder')


class FeaturedCompany(models.Model):

    class Meta :
        verbose_name_plural = 'Featured companies' 

    picture = models.ForeignKey('FeaturedPicture', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)


class ShopPicture(models.Model):
    picture = CloudinaryField('image')
    

class ShopDescription(models.Model):

    class Meta :
        verbose_name_plural = 'Shop Description'

    picture = models.ForeignKey(ShopPicture, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000, null=True, blank=True)
