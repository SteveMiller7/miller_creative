from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('featured_work/', views.Inspiration.as_view(), name='photos'),
    path('shop/', views.ShopDesc.as_view(), name='shop'),
    path('flyer_sizes/', views.FlyerSize.as_view(), name='flyers'),
    
]