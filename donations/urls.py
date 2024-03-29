from unicodedata import name
from django.urls import path
from .views import donations, donationdetail

urlpatterns = [
    path('donations/', donations, name='donations'),
    path('donationdetail/<slug:slug>', donationdetail, name='donationdetail'),
]