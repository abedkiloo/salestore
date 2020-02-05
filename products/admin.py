from django.contrib import admin
from .models import Products
from .models import Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OffersAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


admin.site.register(Products, ProductAdmin)
admin.site.register(Offer, OffersAdmin)
