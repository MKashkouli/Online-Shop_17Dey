from django.contrib import admin
from .models import Product, Comment


class CommentsInline(admin.TabularInline):  # Or class CommentsInline(admin.StackedInline):
    model = Comment
    fields = ("author", "body", "recommend", "active",)
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "active")
    list_filter = ['active']
    list_editable = ['active']
    search_fields = ['title']
    sortable_by = ['price']

    inlines = [CommentsInline]


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("author", "product", "body", "recommend", "active", "datetime_created")
