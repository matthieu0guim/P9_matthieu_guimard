from django.http import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Band, Listing
from listings.form import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail
from django.contrib import messages


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {'bands': bands})

def band_detail(request, band_id):
    band = Band.objects.get(id = band_id)
    return render(request,
        'listings/band_details.html',
        {'band': band}
        
    )

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('band-created')
    else:
        form = BandForm()

    return render(request, 'listings/band_create.html', {'form': form})

def band_creation_confirmation(request):
    return render(request, 'listings/band_creation_confirmation.html')

def band_change(request, band_id):
    band = Band.objects.get(id = band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-list')
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_change.html', {'form': form})

def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        band.delete()
        messages.add_message(request, messages.INFO, 'Le groupe a bien été supprimé.')
        return redirect('band-list')

    return render(request, 'listings/band_delete.html', {'band': band})

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

def create_new_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-created')
    else:
        form = ListingForm()
    
    return render(request, 'listings/list_creation.html', {'form': form})

def listing_creation_confirmation(request):
    return render(request, 'Listings/listing_creation_confirmation.html')

def listing_change(request, list_id):
    listing = Listing.objects.get(id=list_id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing-list')
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_change.html', {'form': form})

def listing_delete(request, list_id):
    listing = Listing.objects.get(id=list_id)
    if request.method == 'POST':
        listing.delete()
        return redirect('listing-list')
    return render(request, 'listings/listing_delete.html', {'listing': listing})

def contact_us(request):
    
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject = f"Message from {form.cleaned_data['name'] or 'anonyme'} via MerchEx Contact us form",
                message = form.cleaned_data["message"],
                from_email = form.cleaned_data["email"],
                recipient_list = ["admin@merchex.xyz"]

            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    
    return render(request, 'listings/contact.html', {'form': form})

def email_confirmation(request):
    return render(request, 'listings/email_sent.html')

