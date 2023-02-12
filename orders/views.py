from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from django.utils.translation import gettext as _
from django.contrib import messages

from .models import Order, OrderItem
from cart.cart import Cart


@login_required
def order_page_view(request):
    cart = Cart(request)
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, _("Your cart is empty"))
        return redirect('products')

    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item["product_obj"]
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item["quantity"],
                    price=product.price,
                )
            cart.clear()

            request.user.first_name=order_obj.first_name
            request.user.last_name=order_obj.last_name
            request.user.save()

            messages.success(request,_("your order has been placed."))

    return render(request, "orders/order_create.html", context={"form": order_form,})
