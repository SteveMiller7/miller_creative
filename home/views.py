from django.shortcuts import render
from django.views import generic
from .models import FeaturedCompany, FeaturedPicture, ShopDescription

def Index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

class FeaturedWork(generic.ListView):
    # The View function for featured work page of site
    model = FeaturedCompany
    template_name = 'featured_work.html'
"""
class Featured(generic.ListView):
    model = FeaturedPicture()
    template_name = 'featured_work.html'
"""

class ShopDesc(generic.ListView):
    model = ShopDescription
    template_name = 'shop.html'
