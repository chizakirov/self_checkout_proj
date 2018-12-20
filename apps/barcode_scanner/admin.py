from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = [
        'sku',
        'name',
        'category',
        'desc',
        'price',
        'vendor',
        'manufacturer',
        'image',
    ]

admin.site.register(Product, ProductAdmin)