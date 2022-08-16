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