from django.contrib import admin
from django.urls import path
from .views import listingListView , listDetailView ,ngoListView, donation_form_receipt
from . import views


urlpatterns = [
    path("" , views.listingListView.as_view(), name= "home"),
    path("user/", ngoListView.as_view() , name='ngo_post'),
    path("<int:pk>/", listDetailView.as_view() , name="list-detail" ),
    path("new-listing", views.fillListForm ,name="new-Requirement"),
    path("receipt/", views.donation_form_receipt ,name="receipt"),
]



