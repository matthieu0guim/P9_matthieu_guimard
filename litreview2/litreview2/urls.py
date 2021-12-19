"""litreview2 URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from litreview import views

import authentication.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name="login"),
    path('register', authentication.views.signup_page, name="signup"),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('flux', views.flux_page, name="flux"),
    path('subscription', views.subscription_page, name='subscribes'),
    path('ticket_creation', views.ticket_creation, name="ticket-creation"),
    path("own_posts", views.own_posts, name='posts'),
    path('review_after_ticket/<int:ticket_id>/', views.review_after_ticket, name='review-after-ticket'),
    path('review_from_scratch', views.review_from_scratch, name='review-from-scratch'),
    path('ticket/<int:ticket_id>/edit', views.edit_ticket, name='edit-ticket'),
    path("own_posts/<int:ticket_id>/delete", views.delete_ticket, name="delete-ticket"),
    path('review/<int:review_id>/edit', views.edit_review, name='edit-review'),
    path('review/<int:review_id>/delete', views.delete_review, name='delete-review'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )