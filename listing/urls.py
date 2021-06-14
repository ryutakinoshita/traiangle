import django.contrib.auth.views
from django.urls import path
from.import views


urlpatterns = [
    path('create/', views.ListingView.as_view(), name='listing_create'),
    path('listing/<slug>/',views.ListingDetailView.as_view(),name='listing_detail'),
    path('additem/<slug>', views.addItem, name='additem'),
    path('order/',views.OrderView.as_view(),name='order'),
    path('removeitem/<slug>', views.removeItem, name='removeitem'),
    path('removesingleitem/<slug>', views.removeSingleItem, name='removesingleitem'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('order/listing', views.OrderListView.as_view(), name='order_listing'),
    ]