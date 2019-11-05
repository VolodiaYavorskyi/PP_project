from django.shortcuts import render, redirect
from .models import Drug, Demand
from django.contrib.auth.decorators import login_required
from . import forms


def drug_list(request):
    drugs = Drug.objects.all()
    return render(request, 'drugs/drug_list.html', {'drugs': drugs})


def drug_detail(request, name):
    drug = Drug.objects.get(name=name)
    return render(request, 'drugs/drug_detail.html', {'drug': drug})


@login_required(login_url="accounts:login")
def drug_create(request):
    if request.method == 'POST':
        form = forms.CreateDrug(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drugs:list')
    else:
        form = forms.CreateDrug()
    return render(request, 'drugs/drug_create.html', {'form': form})


@login_required(login_url="accounts:login")
def drug_update(request, name):
    if request.method == 'POST':
        drug = Drug.objects.get(name=name)
        form = forms.CreateDrug(request.POST)
        if form.is_valid():
            drug.name = form.cleaned_data['name']
            drug.description = form.cleaned_data['description']
            drug.price = form.cleaned_data['price']
            drug.quantity = form.cleaned_data['quantity']
            drug.save()
            return redirect('drugs:list')
    else:
        form = forms.CreateDrug()
    return render(request, 'drugs/drug_update.html', {'form': form})


@login_required(login_url="accounts:login")
def drug_order(request):
    if request.method == 'POST':
        form = forms.CreateOrder(request.POST)
        if form.is_valid():
            drugName = form.cleaned_data['drugName']
            quantity = form.cleaned_data['quantity']
            drug = Drug.objects.get(name=drugName)
            if quantity > drug.quantity:
                dem = Demand()
                dem.drugName = drugName
                dem.save()
            else :
                drug.quantity -= quantity
                drug.save()
            return redirect('drugs:list')
    else:
        form = forms.CreateOrder()
    return render(request, 'drugs/drug_order.html', {'form': form})
