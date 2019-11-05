from django.urls import path
from . import views

app_name = "drugs"

urlpatterns = [
    path('', views.drug_list, name="list"),
    path('create/', views.drug_create, name="create"),
    path('update/<str:name>/', views.drug_update, name="update"),
    path('order/', views.drug_order, name="order"),
    path('<str:name>/', views.drug_detail, name="detail"),
]
