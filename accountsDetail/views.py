from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    IndividualForm,
    ProducerForm,
    RestaurantForm,
    RestaurantImageForm
)
from .models import RestaurantImage


class MyPageView(generic.TemplateView):
    template_name = 'accountsDetail/my_page.html'


class IndividualView(generic.CreateView, LoginRequiredMixin):
    template_name = 'accountsDetail/individual.html'
    form_class = IndividualForm
    success_url = reverse_lazy('signup_finish')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProducerView(generic.CreateView,LoginRequiredMixin):
    template_name = 'accountsDetail/producer.html'
    form_class = ProducerForm
    success_url = reverse_lazy('signup_finish')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RestaurantView(generic.CreateView,LoginRequiredMixin):
    template_name = 'accountsDetail/restaurant.html'
    form_class = RestaurantForm
    success_url = reverse_lazy('restaurant_img')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RestaurantImageView(generic.CreateView,LoginRequiredMixin):  # 投稿機能
    template_name = 'accountsDetail/restaurant_image.html'
    form_class = RestaurantImageForm
    success_url = reverse_lazy('signup_finish')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


