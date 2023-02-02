from django.shortcuts import render


def cart_detail_view(request):
    return render(request, template_name="cart/cart_detail.html")
