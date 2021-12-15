from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
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
        print("coucou")
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            # print(request)
            review.save()
            
            return redirect('flux')
        else:
            print("marche pas")
            pass
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


def own_posts(request, ticket_id=None):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    flux = sorted(list(chain(tickets, reviews)), key=lambda x: x.time_created, reverse=True)
    user = request.user
    delete_form = forms.DeleteTicketForm()
    
    if request.method == 'POST':
        print("coucou")
        ticket = get_object_or_404(Ticket, id=ticket_id)
        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect("posts")
    return render(request, "litreview/own_posts.html", context={'flux': flux, 'user': user, "delete_form": delete_form})

@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('posts')
        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                
                return redirect('posts')
    context = {
        "edit_form": edit_form,
        "delete_form": delete_form,
    }
    return render(request, 'litreview/edit_ticket.html', context=context)

@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect("posts")

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    ticket = get_object_or_404(Ticket, id=review.ticket.id)
    edit_form = forms.ReviewForm(instance=review)
    delete_form = forms.DeleteReviewForm()
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('posts')
        if 'delete_review' in request.POST:
            delete_form = forms.DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.delete()
                
                return redirect('posts')
    context = {
        "edit_form": edit_form,
        "delete_form": delete_form,
        "ticket": ticket,
    }
    return render(request, 'litreview/edit_review.html', context=context)

    

