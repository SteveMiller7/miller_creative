from django.db import models
from cloudinary.models import CloudinaryField


class FeaturedPicture(models.Model):
    picture = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.picture.url

class FeaturedCompany(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ForeignKey(FeaturedPicture, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name