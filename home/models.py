from django.db import models
from cloudinary.models import CloudinaryField



class FeaturedCompany(models.Model):

    class Meta :
        verbose_name_plural = 'Featured companies' 

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


class ShopDescription(models.Model):

    class Meta :
        verbose_name_plural = 'Shop Description'

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)


class FlyerDescription(models.Model):

    class Meta :
        verbose_name_plural = 'Flyer Description'

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
