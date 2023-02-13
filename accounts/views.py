from .models import CustomUser
from .forms import CustomUserChangeForm
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect



# class UserUpdate(generic.CreateView):
#     model = CustomUser
#     form_class = CustomUserChangeForm
#     # fields = ('username', 'email', 'first_name', 'last_name')
#     template_name = "account/profile_update.html.html"
#     success_url = reverse_lazy('profile')

def profile_update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'account/profile_update.html', {'form': form})