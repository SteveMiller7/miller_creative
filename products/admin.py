from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'sku',
        'name',
        'description',
        'size',
        'quantity',
        'price',
        'image_url',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


