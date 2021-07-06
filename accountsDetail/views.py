from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

from listing.models import Listing
from .forms import (
    RestaurantForm,
    ReviewForm,
    ApplicationForm,
)
from .models import Restaurant
from django.views.generic import View

class MyPageView(LoginRequiredMixin,generic.TemplateView):
    """マイページ"""
    template_name = 'accountsDetail/my_page.html'


class RestaurantView(LoginRequiredMixin,generic.CreateView):
    """レストラン登録"""
    template_name = 'accountsDetail/restaurant.html'
    form_class = RestaurantForm
    success_url = reverse_lazy('my_page_restaurant')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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


class ApplicationView(FormView):
    template_name = 'accountsDetail/application.html'
    form_class = ApplicationForm
    success_url = reverse_lazy('application_done')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

class ApplicationDoneView(generic.TemplateView):
    template_name = 'accountsDetail/application_done.html'

class RestaurantMyPageView(LoginRequiredMixin,generic.TemplateView):
    """レストランマイページ"""
    template_name = 'accountsDetail/restaurant_my_page.html'


class RestaurantDetailView(LoginRequiredMixin,generic.DetailView):
    """レストラン詳細"""
    model = Restaurant
    template_name = 'accountsDetail/restaurant_detail.html'
    context_object_name = 'restaurants'



class LikeBase(LoginRequiredMixin, View):
    """お気に入りベース"""
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        related_like = Restaurant.objects.get(pk=pk)

        if self.request.user in related_like.like.all():
            obj = related_like.like.remove(self.request.user)
        else:
            obj = related_like.like.add(self.request.user)
        return obj


class RestaurantLikeDetail(LikeBase):
    """詳細ページでお気に入りした場合"""
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return redirect('restaurant_like_list')


class RestaurantLikeListView(LoginRequiredMixin,generic.ListView):
    """お気に入りレストラン一覧"""
    model = Restaurant
    template_name = 'accountsDetail/restaurant_like_list.html'
    context_object_name = 'item_data'