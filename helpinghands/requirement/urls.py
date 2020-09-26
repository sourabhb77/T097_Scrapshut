from django.contrib import admin
from django.urls import path
from .views import listingListView
from . import views


urlpatterns = [
    path("" , views.listingListView.as_view(), name= "home"),
    path("logout" , views.fillListForm , name ="logout"),
    path("new_listing" , views.fillListForm , name ="listing"),
    path("new_listings" , views.fillListForm , name ="login"),
    path("new_listings2" , views.fillListForm , name ="register"),
]



