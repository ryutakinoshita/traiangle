from django.urls import path,include
from.import views


urlpatterns = [
    path('create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/',views.RecipeDetailView.as_view(),name='recipe_detail'),
]