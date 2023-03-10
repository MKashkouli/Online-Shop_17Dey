from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import uuid

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("user"))
    is_paid = models.BooleanField(default=False)

    first_name = models.CharField(max_length=100, verbose_name=_("first name"))
    last_name = models.CharField(max_length=100, verbose_name=_("last name"))
    phone_number = models.CharField(max_length=15, verbose_name=_("Phone Number"))
    address = models.CharField(max_length=700, verbose_name=_("Address"))
    order_notes = models.CharField(max_length=700,blank=True, verbose_name=_("Order Note"))
    unique_code = models.CharField(max_length=36, default=uuid.uuid4, editable=False, blank=True)

    zarinpal_authority = models.CharField(max_length=255, blank=True)
    zarinpal_ref_id = models.CharField(max_length=255, blank=True)
    zarinpal_data = models.TextField(blank=True)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id}"

    def get_total_price(self):
        return sum(item.quantity*item.price for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"OrderItem {self.id} : {self.product} x {self.quantity} (price:{self.price})"

