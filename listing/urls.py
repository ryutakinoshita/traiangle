import django.contrib.auth.views
from django.urls import path
from.import views


urlpatterns = [
    path('create/', views.ListingView.as_view(), name='listing_create'),
    path('application/', views.ListingApplicationView.as_view(), name='listing_application'),
    path('application/finish/', views.ListingApplicationFinishView.as_view(), name='listing_application_finish'),
    path('listing/<slug>/',views.ListingDetailView.as_view(),name='listing_detail'),
    path('additem/<slug>', views.addItem, name='additem'),
    path('order/',views.OrderView.as_view(),name='order')

]