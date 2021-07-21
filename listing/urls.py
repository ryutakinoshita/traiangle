import django.contrib.auth.views
from django.urls import path
from.import views
from .views import LikeHome, LikeDetail,Confirmed

urlpatterns = [
    path('create/', views.ListingView.as_view(), name='listing_create'),
    path('listing/<slug>/',views.ListingDetailView.as_view(),name='listing_detail'),
    path('my/listing/',views.MyListingView.as_view(),name='my_listing'),
    path('listing/update/<slug>/', views.ListingUpdateView.as_view(), name='listing_edit'),
    path('additem/<slug>/', views.addItem, name='additem'),
    path('order/',views.OrderView.as_view(),name='order'),
    path('removeitem/<slug>/', views.removeItem, name='removeitem'),
    path('removesingleitem/<slug>/', views.removeSingleItem, name='removesingleitem'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('order/listing/', views.OrderListView.as_view(), name='order_listing'),
    path('like-home/<int:pk>', LikeHome.as_view(), name='like-home'),
    path('like-detail/<int:pk>', LikeDetail.as_view(), name='like-detail'),
    path('buyer/',views.BuyerListView.as_view(),name='buyer_list'),
    path('confirmed/<int:pk>',Confirmed.as_view(), name='confirmed'),

    ]