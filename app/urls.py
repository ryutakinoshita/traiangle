from django.urls import path
from.import views


urlpatterns=[
    path('', views.HomeView.as_view(), name='home'),
    path('product/list/', views.ProductListView.as_view(), name='product_list'),
    path('product/list/mie/', views.ProductListMieView.as_view(), name='product_mie'),
    path('product/list/siga/', views.ProductListSigaView.as_view(), name='product_siga'),
    path('product/list/kyoto/', views.ProductListKyotoView.as_view(), name='product_kyoto'),
    path('product/list/osaka/', views.ProductListOsakaView.as_view(), name='product_osaka'),
    path('product/list/hyogo/', views.ProductListHyogoView.as_view(), name='product_hyogo'),
    path('product/list/nara/', views.ProductListNaraView.as_view(), name='product_nara'),
    path('product/list/wakayama/', views.ProductListWakayamaView.as_view(), name='product_wakayama'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('cancel/', views.cancel),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/result/', views.ContactResultView.as_view(), name='contact_result'),
    path('contact/rest/', views.ContactRestView.as_view(), name='contact_rest'),
    path('contact/result/rest/', views.ContactResultRestView.as_view(), name='contact_result_rest'),
    path('privacy/policy/', views.PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('terms/user/', views.TermsUserView.as_view(), name='terms_user'),
    path('terms/store/', views.TermsStoreView.as_view(), name='terms_store'),
    path('help/', views.HelpView.as_view(), name='help'),
    path('help/store/', views.HelpStoreView.as_view(), name='help_store'),
    path('game/list/', views.GameListView.as_view(), name='game_list'),
    path('game/post/<int:pk>/', views.GamePostView.as_view(), name='game_post'),
    path('my_page/', views.MyPageDetailView.as_view(), name='my_page'),

]
