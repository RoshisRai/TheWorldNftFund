from unicodedata import name
from django.urls import path
from .views import projects, projectdetail

urlpatterns = [
    path('projects/', projects, name='projects'),
    path('projectdetail/<slug:slug>/', projectdetail, name='projectdetail'),
]