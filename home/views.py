from django.shortcuts import render
from django.views import generic
from .models import FeaturedCompany

def Index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

class FeaturedWork(generic.ListView):
    # The View function for inspiration page of site
    model = FeaturedCompany
    template_name = 'featured_work.html'
