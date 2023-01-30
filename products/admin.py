from django.contrib import admin
from .models import Product, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "active")
    list_filter = ['active']
    list_editable = ['active']
    search_fields = ['title']
    sortable_by= ['price']


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("author", "product", "body","recommend", "active", "datetime_created")