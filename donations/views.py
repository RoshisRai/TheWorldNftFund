from django.shortcuts import render
from .models import Donation
# Create your views here.
def donations(request):
    donations = Donation.objects.all().order_by('-id')
    context = {
        'donations': donations,
    }
    return render(request, 'donations/donations.html', context)

def donationdetail(request, slug):
    donation = Donation.objects.get(slug=slug)
    context = {
        'donation': donation,
    }
    return render(request, 'donations/donationdetail.html', context)