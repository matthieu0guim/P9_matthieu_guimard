from django import forms
from django.forms import widgets
from . import models

class TicketForm(forms.ModelForm):
    edit_ticket = forms.NullBooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']

class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class ReviewForm(forms.ModelForm):
    edit_review = forms.NullBooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']

class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


# class ItemDescription(forms.Form):
#     title = forms.CharField(max_length=100, label="Titre")
#     description = forms.TextInput(label='Description')
#     image = forms.ImageField(label='Image')

# class Review(forms.Form):
#     title = forms.CharField(max_length=150, label="Titre")
#     grade = forms.

# class ReviewCrationForm(forms.Form):
    

    