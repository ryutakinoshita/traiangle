import django.contrib.auth.views
from django.urls import path,include
from.import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/text/', views.SignupTextView.as_view(), name='signup_text'),
    path('signup/finish/', views.SignupFinishView.as_view(), name='signup_finish'),
    path('email/change/', views.EmailChangeView.as_view(), name='email_change'),
    path('email/change/done/', views.EmailChangeDoneView.as_view(), name='email_change_done'),
    path('email/change/complete/<str:token>/', views.EmailChangeCompleteView.as_view(), name='email_change_complete'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_change/done/', views.PasswordDoneView.as_view(), name='password_done'),

]