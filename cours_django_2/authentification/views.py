from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import View


from authentification.forms import LoginForm, SignupForm, UpdateProfilPhotoForm

from . import forms

def logout_user(request):
    logout(request)
    return redirect('login')


def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            message = "Identifiants invalides!"

    return render(request, 'authentification/login.html', context={'form': form, 'message': message})

def signup_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentification/signup.html', context={"form": form})
    

def upload_profile_photo(request):
    form = forms.UpdateProfilPhotoForm(instance=request.user)
    if request.method == 'POST':
        form = forms.UpdateProfilPhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'authentification/update_profile_picture.html', context={'form': form})

