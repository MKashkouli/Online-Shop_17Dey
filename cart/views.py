from django.shortcuts import render, get_object_or_404, redirect

from .cart import Cart
from .forms import AddToCartForm
from products.models import Product


def cart_detail_view(request):
    cart = Cart(request)
    return render(request, template_name="cart/cart_detail.html", context={'cart': cart, })


def add_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity)

    return redirect('cart:cart_detail')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)

    return redirect('cart:cart_detail')