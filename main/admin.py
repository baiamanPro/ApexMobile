from django.contrib import admin
from .models import Product, Specification


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    search_fields = ("value",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_new", "is_hit", "on_sale")
    list_filter = ("is_new", "is_hit", "on_sale")
    search_fields = ("name",)
    filter_horizontal = ("specifications",)