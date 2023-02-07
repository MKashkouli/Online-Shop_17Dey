from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('aboutus', views.AboutUsView.as_view(), name='aboutus'),
    path('contactus', views.ContactUsView.as_view(), name='contactus'),
    path('profile', views.ProfileView.as_view(), name='profile'),

    ]
