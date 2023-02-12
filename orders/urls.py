from django.urls import path
from . import views


urlpatterns = [
    path('create', views.order_page_view, name='order_create'),

    ]
