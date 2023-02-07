from django.urls import path, include
from . import views

urlpatterns = [

    path('set/', views.UserSet.as_view(), name = 'set'),
]