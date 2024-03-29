from django.http import response
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html', {'homeactive': 'active'})

def about(request):
    return render(request, 'home/about.html', {'aboutactive': 'active'})