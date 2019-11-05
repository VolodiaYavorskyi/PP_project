from django.contrib import admin
from .models import Drug, Order, Demand

admin.site.register(Drug)
admin.site.register(Order)
admin.site.register(Demand)
