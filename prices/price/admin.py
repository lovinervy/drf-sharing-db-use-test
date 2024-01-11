from django.contrib import admin

from .models import Product, ProductPrice


admin.site.register(ProductPrice)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    model._meta.verbose_name_plural = 'Продукты'

admin.site.register(Product, ProductAdmin)
