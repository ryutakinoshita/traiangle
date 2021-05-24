import django.contrib.auth.views
from django.urls import path
from.import views


urlpatterns = [
    path('create/', views.ListingView.as_view(), name='listing_create'),
    path('application/', views.ListingView.as_view(), name='listing_application'),
]