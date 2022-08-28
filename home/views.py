from django.shortcuts import render
from django.views import generic
from .models import ShopDescription, FlyerDescription, Photo


def Index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


class Inspiration(generic.ListView):
    # The View function for featured work page of site
    model = Photo
    template_name = 'featured_work.html'


class ShopDesc(generic.ListView):
    model = ShopDescription
    template_name = 'shop.html'


class FlyerSize(generic.ListView):
    model = FlyerDescription
    template_name = 'flyer_sizes.html'
