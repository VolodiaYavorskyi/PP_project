from django import forms
from . import models

class CreateDrug(forms.ModelForm):
    class Meta:
        model = models.Drug
        fields = ['name', 'description', 'price', 'quantity']

class CreateOrder(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['drugName', 'quantity']
