from django.contrib import admin
from .models import Item, Account


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
