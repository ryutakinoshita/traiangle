import django.contrib.auth.views
from django.urls import path,include
from.import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signup/finish/<token>/', views.SignupFinishView.as_view(), name='signup_finish'),
    path('signup/done/', views.SignupDoneView.as_view(), name='user_create_done'),
    path('email/change/', views.EmailChangeView.as_view(), name='email_change'),
    path('email/change/done/', views.EmailChangeDoneView.as_view(), name='email_change_done'),
    path('email/change/complete/<str:token>/', views.EmailChangeCompleteView.as_view(), name='email_change_complete'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_change/done/', views.PasswordDoneView.as_view(), name='password_done'),
    path('update/<int:pk>/', views.UserZipUpdateView.as_view(), name='user_update'),
    path('login/restaurant/', views.RestaurantLoginView.as_view(), name='restaurant_login'),
    path('signup/restaurnt/', views.RestaurantUserCreateView.as_view(), name='restaurant_signup'),
    path('restaurant/finish/<token>/', views.RestaurantFinishView.as_view(), name='restaurant_finish'),
]