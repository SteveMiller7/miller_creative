from django.contrib import admin
from .models import FeaturedCompany, FeaturedPicture, Product, Category


admin.site.register(FeaturedCompany)
admin.site.register(FeaturedPicture)
admin.site.register(Product)
admin.site.register(Category)

