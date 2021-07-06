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
    path('review/<int:pk>/',views.ReviewView.as_view(),name='review'),
    path('like-detail/<int:pk>', RestaurantLikeDetail.as_view(), name='like-restaurant'),

]