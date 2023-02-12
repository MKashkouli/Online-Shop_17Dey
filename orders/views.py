from django.shortcuts import render
from .forms import OrderForm


def order_page_view(request):
    return render(request, "orders/order_create.html", context={"form": OrderForm})
