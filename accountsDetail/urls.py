import django.contrib.auth.views
from django.urls import path
from.import views


urlpatterns = [
    path('restaurant/', views.RestaurantView.as_view(), name='restaurant'),
    path('my_page/', views.MyPageView.as_view(), name='my_page'),
    path('review/<int:pk>/',views.ReviewView.as_view(),name='review'),

]