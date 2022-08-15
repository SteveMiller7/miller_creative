from django.db import models

class Featured_Company (models.Model):
    company = models.CharField(max_length=50)
    company_type = models.CharField(max_length=50)
    featured_image = CloudinaryField('image', default='placeholder')
    date = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=50)


