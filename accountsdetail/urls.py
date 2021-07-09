import django.contrib.auth.views
from django.urls import path
from.import views
from .views import RestaurantLikeDetail

urlpatterns = [
    path('restaurant/', views.RestaurantView.as_view(), name='restaurant'),
    path('restaurant/<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('my_page/', views.MyPageView.as_view(), name='my_page'),
    path('my_page/restaurant/', views.RestaurantMyPageView.as_view(), name='my_page_restaurant'),
    path('like/restaurant/',views. RestaurantLikeListView.as_view(),name='restaurant_like_list'),
    path('application/', views.ApplicationView.as_view(), name='application'),
    path('application/done/', views.ApplicationDoneView.as_view(), name='ApplicationDoneView'),
    # path('review/<int:pk>/',views.ReviewView.as_view(),name='review'),
    path('mie/',views. RestaurantListMieView.as_view(),name='mie'),
    path('siga/',views.RestaurantListSigaView.as_view(),name='siga'),
    path('kyoto/',views.RestaurantListKyotoView.as_view(),name='kyoto'),
    path('osaka/',views.RestaurantListOsakaView.as_view(),name='osaka'),
    path('hyogo/',views.RestaurantListHyogoView.as_view(),name='hyogo'),
    path('nara/',views.RestaurantListNaraView.as_view(),name='nara'),
    path('wakayama/',views.RestaurantListWakayamaView.as_view(),name='wakayama'),
    path('link/',views.RestaurantLinkView.as_view(),name='link'),
    path('my/restaurant/<int:pk>', views.MyRestaurantDetailView.as_view(), name='my_restaurant_detail'),
    path('like-detail/<int:pk>', RestaurantLikeDetail.as_view(), name='like-restaurant'),

]