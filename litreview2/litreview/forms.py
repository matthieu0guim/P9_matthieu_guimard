from django import forms
from django.contrib.auth import get_user_model
from . import models


User = get_user_model()


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


class FollowUsersForm(forms.ModelForm):

    class Meta:
        model = models.UserFollows
        fields = ['followed_user']


class DeleteFollowForm(forms.Form):
    delete_follow = forms.BooleanField(widget=forms.HiddenInput, initial=True)
