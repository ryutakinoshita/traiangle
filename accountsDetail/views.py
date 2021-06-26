from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from listing.models import Listing
from .forms import (
    ProducerForm,
    RestaurantForm,
    RestaurantImageForm,
    ReviewForm

)


class MyPageView(LoginRequiredMixin,generic.TemplateView):
    """マイページ"""
    template_name = 'accountsDetail/my_page.html'


class ProducerView(LoginRequiredMixin,generic.CreateView):
    """生産者登録"""
    template_name = 'accountsDetail/producer.html'
    form_class = ProducerForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RestaurantView(LoginRequiredMixin,generic.CreateView):
    """レストラン登録"""
    template_name = 'accountsDetail/restaurant.html'
    form_class = RestaurantForm
    success_url = reverse_lazy('restaurant_img')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RestaurantImageView(LoginRequiredMixin,generic.CreateView):
    """レストラン写真"""
    template_name = 'accountsDetail/restaurant_image.html'
    form_class = RestaurantImageForm
    success_url = reverse_lazy('signup_finish')

    def form_valid(self, form):
        form.instance.restaurant=self.request.user
        return super().form_valid(form)

#
class ReviewView(LoginRequiredMixin,generic.CreateView):
    template_name = 'accountsDetail/review.html'
    form_class = ReviewForm


    def form_valid(self, form ):
        form.instance.user = self.request.user
        listing_pk = self.kwargs['pk']
        listing = get_object_or_404(Listing, pk=listing_pk)
        review = form.save(commit=False)
        review.target = listing
        review.save()
        return redirect('home',pk=listing_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listing'] = get_object_or_404(Listing, pk=self.kwargs['pk'])
        return context