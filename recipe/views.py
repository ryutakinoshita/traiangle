from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from recipe.forms import (
    RecipeCreateForm
)
from recipe.models import Recipe


class RecipeCreateView(LoginRequiredMixin,generic.CreateView):
    """レシピ投稿機能"""
    template_name = 'recipe/recipe_create.html'
    form_class = RecipeCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecipeListView(LoginRequiredMixin,generic.ListView):
    """レシピ一覧"""
    model = Recipe
    template_name = 'recipe/recipe_list.html'
    context_object_name = 'recipe'

class RecipeDetailView(LoginRequiredMixin,generic.DetailView):
    """レシピ詳細"""
    model = Recipe
    template_name = 'recipe/recipe_detail.html'