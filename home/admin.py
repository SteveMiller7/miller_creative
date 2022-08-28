from django.contrib import admin
from .models import ShopDescription, FlyerDescription, Photo


admin.site.register(ShopDescription)
admin.site.register(FlyerDescription)
admin.site.register(Photo)