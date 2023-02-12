from django.shortcuts import render


def order_page_view(request):
    return render(request, "orders/order_create.html")
