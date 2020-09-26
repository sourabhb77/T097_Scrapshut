from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.require_form,name="requirement-form"),
    path('receipt/',views.receipt,name="receipt")
]



