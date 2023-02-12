from django import forms
from .models import Order
from django.utils.translation import gettext_lazy as _


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [_('first_name'), _('last_name'), _('phone_number'), _('address'), _('order_notes')]
        widgets = {
            "address": forms.Textarea(attrs={'rows': 3}),
            "order_notes": forms.Textarea(attrs={
                'rows': 3,
                "placeholder": 'if you have any notes please mention it otherwise leave it empty'}),
                  }