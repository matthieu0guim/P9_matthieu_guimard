from django import forms
from django.forms import fields

from listings.models import Band, Listing

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class BandForm(forms.ModelForm):
    class Meta():
        model = Band
        exclude = ('active', 'official_homepage')

class ListingForm(forms.ModelForm):
    class Meta():
        model = Listing
        fields = '__all__'