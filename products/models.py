from django.db import models


class Picture(models.Model):
    picture = models.ImageField(upload_to='media/images')  

    def __str__(self):
        return self.picture.url
        

class BusinessCards(models.Model):

    qty_list = (
        (0, '100'),
        (1, '250'),
        (2, '500'),
        (3, '1000'),
        (4, '2500'),

    )

    lam_finish = (
        (0, 'Matt'),
        (1, 'Gloss'),
        (2, 'Soft Touch, Velvet'),

    )

    name = models.CharField(max_length=200)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    quantity = models.IntegerField(choices=qty_list)
    lamination = models.IntegerField(choices=lam_finish)

 
    def __str__(self):
        return self.name
