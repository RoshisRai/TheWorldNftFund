from unicodedata import name
from django.urls import path
from .views import writings, writingdetail

urlpatterns = [
    path('writings/', writings, name='writings'),
    path('writingdetail/<slug:slug>/', writingdetail, name='writingdetail'),
]