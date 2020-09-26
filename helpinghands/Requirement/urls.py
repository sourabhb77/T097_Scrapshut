from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.require_form,name="requirement-form"),
    path('receipt/',views.receipt,name="receipt"),
    path('donation-form/',views.donation_form,name="donation-form"),
    path('donation-form/donation-form-receipt/',views.donation_form_receipt,name="donation-form-receipt")
]



