from django.urls import path
from.import views


urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('app/',views.AppView.as_view(),name='app'),
    path('product/list/',views.ProductListView.as_view(),name='product_list'),
    path('product/list/mie/',views.ProductListMieView.as_view(),name='product_mie'),
    path('product/list/siga/',views.ProductListSigaView.as_view(),name='product_siga'),
    path('product/list/kyoto/',views.ProductListKyotoView.as_view(),name='product_kyoto'),
    path('product/list/osaka/',views.ProductListOsakaView.as_view(),name='product_osaka'),
    path('product/list/hyogo/',views.ProductListHyogoView.as_view(),name='product_hyogo'),
    path('product/list/nara/',views.ProductListNaraView.as_view(),name='product_nara'),
    path('product/list/wakayama/',views.ProductListWakayamaView.as_view(),name='product_wakayama'),
    path('index/', views.index, name='subscriptions-index'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('cancel/', views.cancel),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/result/', views.ContactResultView.as_view(), name='contact_result'),
]
