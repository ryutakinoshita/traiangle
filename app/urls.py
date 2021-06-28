from django.urls import path
from.import views


urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('product/list/',views.ProductListView.as_view(),name='product_list'),
    path('product/list/vegetables/',views.ProductListVegetablesView.as_view(),name='product_vegetables'),
    path('product/list/fruits/',views.ProductListFruitsView.as_view(),name='product_fruits'),
    path('product/list/fish/',views.ProductListFishView.as_view(),name='product_fish'),
    path('product/list/meat/',views.ProductListMeatView.as_view(),name='product_meat'),
    path('product/list/dairy/',views.ProductListDairyView.as_view(),name='product_dairy'),
    path('product/list/processing/',views.ProductListProcessingView.as_view(),name='product_processing'),
    path('product/list/drink/',views.ProductListDrinkView.as_view(),name='product_drink'),
    path('product/list/alcohol/',views.ProductListAlcoholView.as_view(),name='product_alcohol'),
    path('product/list/other/',views.ProductListOtherView.as_view(),name='product_other'),
    path('index/', views.index, name='subscriptions-index'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('cancel/', views.cancel),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/result/', views.ContactResultView.as_view(), name='contact_result'),
]
