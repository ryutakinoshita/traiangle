from django.urls import path,include
from.import views
from .views import GoodDetail

urlpatterns = [
    path('create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('list/Free/', views.RecipeListFreeView.as_view(), name='recipe_free'),
    path('list/time/', views.RecipeListTimeView.as_view(), name='recipe_time'),
    path('recipe/<int:pk>/',views.RecipeDetailView.as_view(),name='recipe_detail'),
    path('good-detail/<int:pk>',GoodDetail.as_view(), name='good-detail'),
]