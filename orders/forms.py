from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name','last_name',"phone_number","address","order_notes" )
        widgets = {
            "address": forms.Textarea(attrs={'rows': 3}),
            "order_notes": forms.Textarea(attrs={'rows': 3, "placeholder": 'if you have any notes please mention it otherwise leave it empty'}),

        }