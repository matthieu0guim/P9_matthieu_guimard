from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from litreview.forms import ReviewForm, TicketForm
from litreview.models import User, Ticket, Review, UserFollows
from . import forms

from itertools import chain

def sign_in_page(request):
    return render(
        request,
        "litreview/sign_in.html"
    )

@login_required
def flux_page(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    flux = sorted(list(chain(tickets, reviews)), key=lambda x: x.time_created, reverse=True)
    print(flux)

    return render(request, "litreview/flux.html", context={'flux': flux})

@login_required
def subscription_page(request):
    return render(
        request,
        "litreview/subscription.html"
    )

@login_required
def ticket_creation(request): # will handle ticket modification as one with an id already attributed
    form = forms.TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux')
    return render(request, "litreview/ticket_creation.html", context={'form': form})

@login_required
def review_after_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            print(request)
            review.save()
            return redirect('flux')
    return render(request, 'litreview/review_after_ticket.html', context={"ticket": ticket, 'form': form})

@login_required
def review_from_scratch(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False) 
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('flux')
    return render(request, 'litreview/review_from_scratch.html', context={"ticket_form": ticket_form, "review_form": review_form})





def review_creation(request): # will handle review modification as one with an id already attributed
    return render(
        request,
        "litreview/review_creation.html"
    )


def own_posts(request):
    return render(
        request,
        "litreview/own_posts.html"
    )
