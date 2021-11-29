from django.http import HttpResponse
from django.shortcuts import render

from litreview.models import User, Ticket, Review, UserFollows



def sign_in_page(request):
    return render(
        request,
        "litreview/sign_in.html"
    )


def flux_page(request):
    return render(
        request,
        "litreview/flux.html"
    )


def subscription_page(request):
    return render(
        request,
        "litreview/subscription.html"
    )


def ticket_creation(request): # will handle ticket modification as one with an id already attributed
    return render(
        request,
        "litreview/ticket_creation.html"
    )


def review_creation(request): # will handle review modification as one with an id already attributed
    return render(
        request,
        "litreview/review_craetion.html"
    )


def own_posts(request):
    return render(
        request,
        "litreview/own_posts.html"
    )
