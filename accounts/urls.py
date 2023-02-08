from django.urls import path, include
from . import views

urlpatterns = [

    path('update/', views.UserUpdate.as_view(), name = 'update'),
]