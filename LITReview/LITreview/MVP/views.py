from django.http import HttpResponse
from django.shortcuts import render

from MVP.models import User, Ticket, Review, UserFollows

def log_page(request):
    return render(
        request,
        "MVP/log_page.html"
    )

def sign_in_page(request):
    return render(
        request,
        "MVP/sign_in.html"
    )

def flux_page(request):
    return render(
        request,
        "MVP/flux.html"
    )

def subscription_page(request):
    return render(
        request,
        "MVP/subscription.html"
    )

def ticket_creation(request): # will handle ticket modification as one with an id already attributed
    return render(
        request,
        "MVP/ticket_creation.html"
    )

def review_creation(request): # will handle review modification as one with an id already attributed
    return render(
        request,
        "MVP/review_craetion.html"
    )

def own_posts(request):
    return render(
        request,
        "MVP/own_posts.html"
    )
