from django import forms
from .models import Item, Account

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'image', 'content', 'price', 'amount', 'account']

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'call', 'address',]