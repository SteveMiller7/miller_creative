from django.contrib import admin
from .models import FeaturedCompany, ShopDescription, FlyerDescription, Photo


admin.site.register(FeaturedCompany)
admin.site.register(ShopDescription)
admin.site.register(FlyerDescription)
admin.site.register(Photo)