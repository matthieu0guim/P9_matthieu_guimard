from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def band_list(request):
    bands = Band.objects.all()
    #return render(request, "C:\Users\Utilisateur\OneDrive - solarisbi\Bureau\openclassroom\dev_python\P9_matthieu_guimard\cours_django_1\merchex\listings\hello.html")
    return render(request, "listings/band_list.html", {'bands': bands})

def band_detail(request, band_id):
    band = Band.objects.get(id = band_id)
    return render(request,
        'listings/band_details.html',
        {'band': band}
        
    )

def about(request):
    return render(request, 'listings/about.html')

def listings(request):
    lists = Listing.objects.all()
    return render(request, 'listings/listings.html', {'lists': lists})

def list_detail(request, list_id):
    liste = Listing.objects.get(id = list_id)
    return render(
        request,
        'listings/list_details.html',
        {'list': liste}
    )

def contact_us(request):
    return render(request, 'listings/contact.html')
