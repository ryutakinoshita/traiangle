from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from recipe.forms import (
    RecipeCreateForm
)


class RecipeCreateView(LoginRequiredMixin,generic.CreateView):  # 投稿機能
    template_name = 'recipe/recipe_create.html'
    form_class = RecipeCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)