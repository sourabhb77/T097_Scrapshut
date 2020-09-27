from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register ,name='accounts-register'),
    path('register_ngo/', views.register_ngo ,name='accounts-register-ngo'),
    path('about/', views.about ,name='accounts-about'),
    path('login/', views.login ,name='login'),
    path('logout/', views.logout ,name='accounts-logout'),
    path('description/', views.description ,name='product-description'),
    path("register/" , views.register , name ="register"),
    path("receipt/" , views.donation_form_receipt , name ="receipt"),
    
]