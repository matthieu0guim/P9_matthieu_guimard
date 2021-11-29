"""fotoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView, PasswordChangeView

import authentification.views # comme il y a plusieurs apps, il va ya voir plusieurs fichier views. Il vaut donc mieux garder le chemin complet
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentification.views.login_page, name="login"),
    path('password_change', PasswordChangeView.as_view(), name='password-change'),
    path('password_changed', PasswordChangeDoneView.as_view(
        template_name='blog/home.html'),
        name='password_change_done'),
    # path('logout/', authentification.views.logout_user, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register', authentification.views.signup_page, name="signup"),
    path('blog/', blog.views.home, name="home"),
]
