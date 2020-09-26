from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register ,name='accounts-register'),
    path('register_ngo/', views.register_ngo ,name='accounts-register-ngo'),
    path('about/', views.about ,name='accounts-about'),
    path('login/', views.login ,name='accounts-login'),
    path('logout/', views.logout ,name='accounts-logout'),
    path('home/', views.home ,name='accounts-home'),
    path('description/', views.description ,name='product-description'),

]
