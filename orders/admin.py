from django.contrib import admin
from .models import Order, OrderItem
from jalali_date.admin import ModelAdminJalaliMixin


class OrderInline(admin.TabularInline):  # Or class CommentsInline(admin.StackedInline):
    model = OrderItem
    fields = ("order", "product", "quantity", "price",)
    extra = 2

@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "datetime_created", "is_paid")

    inlines = [OrderInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "price",)
