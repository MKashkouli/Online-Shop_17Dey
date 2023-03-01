from django.views import generic
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from .models import Product, Comment
from cart.forms import AddToCartForm
from django.contrib import messages
from django.utils.translation import gettext as _
from django.db.models import F


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)  # or model = Product
    paginate_by = 8
    template_name = "products/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by')
        order_by = self.request.GET.get('order_by', 'asc')

        queryset = super().get_queryset()

        if sort_by == 'price':
            queryset = queryset.order_by(
                F('price').asc(nulls_last=True) if order_by == 'asc'
                else F('price').desc(nulls_last=True))
        elif sort_by == 'recently_added':
            queryset = queryset.order_by(
                F('datetime_created').asc(nulls_last=True) if order_by == 'asc'
                else F('datetime_created').desc(nulls_last=True))

        return queryset


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        # context['add_to_cart_form'] = AddToCartForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product
        messages.success(self.request, _("Your Comment added Successfully"))
        return super().form_valid(form)
