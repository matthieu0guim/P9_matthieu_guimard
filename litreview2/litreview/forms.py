from django import forms
from django.forms import widgets
from . import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']

class ReviewForm(forms.ModelForm):
    # title = forms.CharField(max_length=128,widget=widgets.TextInput, label='')
    # descritpion = forms.CharField(max_length=8192, widget=widgets.TextInput, label='')
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']


# class ItemDescription(forms.Form):
#     title = forms.CharField(max_length=100, label="Titre")
#     description = forms.TextInput(label='Description')
#     image = forms.ImageField(label='Image')

# class Review(forms.Form):
#     title = forms.CharField(max_length=150, label="Titre")
#     grade = forms.

# class ReviewCrationForm(forms.Form):
    

    