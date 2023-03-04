from django.contrib import admin
from .models import Product, Comment,Wishlist
from jalali_date.admin import ModelAdminJalaliMixin


class CommentsInline(admin.TabularInline):  # Or class CommentsInline(admin.StackedInline):
    model = Comment
    fields = ("author", "body", "recommend", "active",)
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin ,admin.ModelAdmin):
    list_display = ("title", "price", "active")
    list_filter = ['active']
    list_editable = ['active']
    search_fields = ['title']
    sortable_by = ['price']

    inlines = [CommentsInline]


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("author", "product", "body", "recommend", "active", "datetime_created")


@admin.register(Wishlist)
class Wishlist(admin.ModelAdmin):
    list_display = ("user",)
