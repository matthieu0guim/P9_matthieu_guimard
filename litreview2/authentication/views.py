from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render

from authentication.forms import LoginForm, SignupForm


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
                return redirect('flux')
            message = "Identifiants invalides!"

    return render(request, 'authentication/login.html', context={'form': form, 'message': message})

def signup_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={"form": form})