import django.contrib.auth.views
from django.urls import path
from.import views


urlpatterns = [
    path('producer/', views.ProducerView.as_view(), name='producer'),
    path('restaurant/', views.RestaurantView.as_view(), name='restaurant'),
    path('my_page/', views.MyPageView.as_view(), name='my_page'),
    path('restaurant/img/', views.RestaurantImageView.as_view(), name='restaurant_img'),
    path('review/<int:pk>/',views.ReviewView.as_view(),name='review'),

]