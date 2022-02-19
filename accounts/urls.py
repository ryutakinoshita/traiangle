import django.contrib.auth.views
from django.urls import path,include
from.import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signup/finish/<token>/', views.SignupFinishView.as_view(), name='signup_finish'),
    path('signup/done/', views.SignupDoneView.as_view(), name='user_create_done'),

]