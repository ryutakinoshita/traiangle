from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    ProducerForm,
    RestaurantForm,
    RestaurantImageForm

)


class MyPageView(generic.TemplateView):
    """マイページ"""
    template_name = 'accountsDetail/my_page.html'


class ProducerView(generic.CreateView,LoginRequiredMixin):
    """生産者登録"""
    template_name = 'accountsDetail/producer.html'
    form_class = ProducerForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RestaurantView(generic.CreateView,LoginRequiredMixin):
    """レストラン登録"""
    template_name = 'accountsDetail/restaurant.html'
    form_class = RestaurantForm
    success_url = reverse_lazy('restaurant_img')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RestaurantImageView(generic.CreateView,LoginRequiredMixin):
    """レストラン写真"""
    template_name = 'accountsDetail/restaurant_image.html'
    form_class = RestaurantImageForm
    success_url = reverse_lazy('signup_finish')

    def form_valid(self, form):
        form.instance.restaurant=self.request.user
        return super().form_valid(form)


