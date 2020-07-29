from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Item, Account
from .forms import ItemForm, AccountForm

# Create your views here.
def item_list(request):
    item_list = Item.objects.all()
    context = {'item_list': item_list}
    return render(request, 'inventory/item_list.html', context)

def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    context = {
        'item': item
    }
    return render(request, 'inventory/item_detail.html', context)

def item_register(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            pk = item.id
            url = reverse('inventory:item_detail', kwargs={'pk': pk})
            return redirect(to=url)
    else:
        form = ItemForm
    context = {'form': form}
    return render(request, 'inventory/item_register.html', context)

def item_update(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            pk = item.id
            url = reverse('inventory:item_detail', kwargs={'pk': pk})
            return redirect(to=url)
    else:
        form = ItemForm(instance=item)
    context = {'form': form}
    return render(request, 'inventory/item_register.html', context)


def item_delete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return redirect('inventory:item_list')


def account_list(request):
    account_list = Account.objects.all()
    context = {'account_list': account_list}
    return render(request, 'inventory/account_list.html', context)

def account_detail(request, pk):
    account = Account.objects.get(id=pk)
    context = {
        'account': account
    }
    return render(request, 'inventory/account_detail.html', context)

def account_register(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            pk = account.id
            url = reverse('inventory:account_detail', kwargs={'pk': pk})
            return redirect(to=url)
    else:
        form = AccountForm
    context = {'form': form}
    return render(request, 'inventory/account_register.html', context)


def account_update(request, pk):
    account = Account.objects.get(id=pk)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance= account)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            pk = account.id
            url = reverse('inventory:account_detail', kwargs={'pk': pk})
            return redirect(to=url)
    else:
        form = AccountForm(instance=account)
    context = {'form': form}
    return render(request, 'inventory/account_register.html', context)


def account_delete(request, pk):
    account = Account.objects.get(id=pk)
    account.delete()
    return redirect('inventory:account_list')