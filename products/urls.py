from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.ProductListView.as_view(), name='products'),
    path('<int:pk>/',views.ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>/',views.CommentCreateView.as_view(), name='comment_create'),
    path('add_to_wishlist/<int:pk>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.view_wishlist, name='view_wishlist'),
]
