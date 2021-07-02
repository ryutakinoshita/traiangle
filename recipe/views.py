from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from recipe.forms import (
    RecipeCreateForm
)
from recipe.models import Recipe
from django.views.generic import View
from django.shortcuts import redirect
from django.db.models import Q


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
    queryset = Recipe.objects.order_by('add_time')


class RecipeListFreeView(LoginRequiredMixin,generic.ListView):
    """タグ検索レシピ一覧"""
    model = Recipe
    template_name = 'recipe/recipe_free_list.html'
    context_object_name = 'recipe'

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Recipe.objects.filter(
                Q(food_tag__icontains=q_word)
            )
        else:
            object_list = Recipe.objects.order_by('?')
        return object_list

class RecipeListTimeView(LoginRequiredMixin,generic.ListView):
    """時間検索レシピ一覧"""
    model = Recipe
    template_name = 'recipe/recipe_time_list.html'
    context_object_name = 'recipe'

    def get_queryset(self):
        q_data = self.request.GET.get('data')
        if q_data:
            object_list = Recipe.objects.filter(
                Q(recipe_time__icontains=q_data)
            )
        else:
            object_list = Recipe.objects.order_by('?')
        return object_list

class RecipeDetailView(LoginRequiredMixin,generic.DetailView):
    """レシピ詳細"""
    model = Recipe
    template_name = 'recipe/recipe_detail.html'


class GoodBase(LoginRequiredMixin,View):
    """myレシピベース"""
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        related_good = Recipe.objects.get(pk=pk)

        if self.request.user in related_good.good.all():
            obj = related_good.good.remove(self.request.user)
        else:
            obj = related_good.good.add(self.request.user)
        return obj


class GoodDetail(GoodBase):
    """詳細ページでmyレシピした場合"""
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return redirect('like_list')

