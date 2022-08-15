from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('featured_work/', views.FeaturedWork.as_view(), name='featured'),
]