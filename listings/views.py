from django.shortcuts import render, get_object_or_404
from .models import Listing

def home(request):
    listings = Listing.objects.filter(is_active=True)
    return render(request, 'listings/index.html', {'listings': listings})

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk, is_active=True)
    return render(request, 'listings/detail.html', {'listing': listing})
