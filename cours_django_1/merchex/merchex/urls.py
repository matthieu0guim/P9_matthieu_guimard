"""merchex URL Configuration

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
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:band_id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_create, name='band-create'),
    path('bands/band-creation-confirmation/', views.band_creation_confirmation, name='band-created'),
    path('bands/<int:band_id>/delete/', views.band_delete, name='band-delete'),
    path('about-us/', views.about, name='about'),
    path('listings/', views.listings, name='listing-list'),
    path('listings/<int:list_id>', views.list_detail, name='list-detail'),
    path('listings/create_new_listing', views.create_new_listing, name='list-create'),
    path('listings/listing_creation_confirmation', views.listing_creation_confirmation, name='list-created'),
    path('listings/<int:list_id>/change', views.listing_change, name='listing-change'),
    path('listings/<int:list_id>/delete', views.listing_delete, name="listing-delete"),
    path('contact us/',views.contact_us , name='contact'),
    path('mail-confirmation/', views.email_confirmation, name='email-sent'),
    path('bands/<int:band_id>/change', views.band_change, name='band-change')
    ]
