from .models import CustomUser
from .forms import CustomUserChangeForm
from django.views import generic
from django.urls import reverse_lazy


class UserUpdate(generic.CreateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    # fields = ('username', 'email', 'first_name', 'last_name')
    template_name = "account/set.html"
    success_url = reverse_lazy('profile')
