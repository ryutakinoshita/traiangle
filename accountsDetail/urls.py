import django.contrib.auth.views
from django.urls import path
from.import views


urlpatterns = [
    path('individual/', views.IndividualView.as_view(), name='individual'),
    path('producer/', views.ProducerView.as_view(), name='producer'),
    path('restaurant/', views.RestaurantView.as_view(), name='restaurant'),
    path('my_page/', views.MyPageView.as_view(), name='my_page'),
]