from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    IndividualForm,
    ProducerForm,
    RestaurantForm
)

class MyPageView(generic.TemplateView):
    template_name = 'accountsDetail/my_page.html'


class IndividualView(generic.CreateView, LoginRequiredMixin):
    template_name = 'accountsDetail/individual.html'
    form_class = IndividualForm
    success_url = reverse_lazy('signup_finish')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProducerView(generic.CreateView, LoginRequiredMixin):
    template_name = 'accountsDetail/producer.html'
    form_class = ProducerForm
    success_url = reverse_lazy('signup_finish')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RestaurantView(generic.CreateView, LoginRequiredMixin):
    template_name = 'accountsDetail/restaurant.html'
    form_class = RestaurantForm
    success_url = reverse_lazy('signup_finish')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)