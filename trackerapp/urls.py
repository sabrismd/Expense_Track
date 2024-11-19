from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('category',views.get_category),
    path('category/add',views.add_category),
    path('expense/add',views.add_expense)
]