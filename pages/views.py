from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutUsView(TemplateView):
    template_name = "aboutus.html"


class ContactUsView(TemplateView):
    template_name = "contactus.html"


class ProfileView(TemplateView):
    template_name = "profile.html"