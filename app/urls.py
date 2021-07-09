from django.urls import path
from.import views


urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('product/list/',views.ProductListView.as_view(),name='product_list'),
    path('index/', views.index, name='subscriptions-index'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('cancel/', views.cancel),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/result/', views.ContactResultView.as_view(), name='contact_result'),
]
