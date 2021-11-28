from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout

from authentification.forms import LoginForm


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
