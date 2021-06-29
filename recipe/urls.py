from django.urls import path,include
from.import views


urlpatterns = [
    path('create/', views.RecipeCreateView.as_view(), name='recipe_create'),

]