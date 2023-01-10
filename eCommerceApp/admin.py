from django.contrib import admin
from .models import (
    Products,
    ProductCategory,
    Banner,
    ProductFeedback,
    ProductOrder,
    ShopingCart
)


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ("user", "title", "price", "image",)

# Register your models here.
admin.site.register(Products)
admin.site.register(ProductCategory)
admin.site.register(Banner)
admin.site.register(ProductFeedback)
admin.site.register(ProductOrder)
admin.site.register(ShopingCart)

