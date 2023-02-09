from django.urls import path, include
from . import views

urlpatterns = [

    path('profile/update/', views.profile_update, name='profile_update'),

]