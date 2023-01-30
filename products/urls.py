from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.ProductListView.as_view(), name='products'),
    path('<int:pk>/',views.ProductDetailView.as_view(), name='product_detail'),
]
