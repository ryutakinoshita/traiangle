from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.db.models import Q

from accounts.models import User
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


class RestaurantListMieView(LoginRequiredMixin,generic.ListView):
    """Mie"""
    model = Restaurant
    template_name = 'accountsDetail/restaurant_Mie.html'
    context_object_name = 'restaurant'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        q_type = self.request.GET.get('type')
        if q_word:
            object_list = Restaurant.objects.filter(
                Q(restaurant_name__icontains=q_word) | Q(certification__icontains=q_word)
            )
        elif q_data:
            object_list=Restaurant.objects.filter(
                Q(nearest_station__icontains=q_data)| Q(city__icontains=q_data)| Q(address1__icontains=q_data)
            )
        elif q_type:
            object_list=Restaurant.objects.filter(
                Q(restaurant_type__icontains=q_type)
            )
        else:
            object_list = Restaurant.objects.filter(prefectures="1")
        return object_list.filter(prefectures="1")


class RestaurantListSigaView(LoginRequiredMixin,generic.ListView):
    """Siga"""
    model = Restaurant
    template_name = 'accountsDetail/restaurant_Siga.html'
    context_object_name = 'restaurant'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        q_type = self.request.GET.get('type')
        if q_word:
            object_list = Restaurant.objects.filter(
                Q(restaurant_name__icontains=q_word) | Q(certification__icontains=q_word)
            )
        elif q_data:
            object_list=Restaurant.objects.filter(
                Q(nearest_station__icontains=q_data)| Q(city__icontains=q_data)| Q(address1__icontains=q_data)
            )
        elif q_type:
            object_list=Restaurant.objects.filter(
                Q(restaurant_type__icontains=q_type)
            )
        else:
            object_list = Restaurant.objects.filter(prefectures="2")
        return object_list.filter(prefectures="2")


class RestaurantListKyotoView(LoginRequiredMixin,generic.ListView):
    """Kyoto"""
    model = Restaurant
    template_name = 'accountsDetail/restaurant_Kyoto.html'
    context_object_name = 'restaurant'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        q_type = self.request.GET.get('type')
        if q_word:
            object_list = Restaurant.objects.filter(
                Q(restaurant_name__icontains=q_word) | Q(certification__icontains=q_word)
            )
        elif q_data:
            object_list=Restaurant.objects.filter(
                Q(nearest_station__icontains=q_data)| Q(city__icontains=q_data)| Q(address1__icontains=q_data)
            )
        elif q_type:
            object_list=Restaurant.objects.filter(
                Q(restaurant_type__icontains=q_type)
            )
        else:
            object_list = Restaurant.objects.filter(prefectures="3")
        return object_list.filter(prefectures="3")



class RestaurantListOsakaView(LoginRequiredMixin,generic.ListView):
    """Osaka"""
    model = Restaurant
    template_name = 'accountsDetail/restaurant_Osaka.html'
    context_object_name = 'restaurant'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        q_type = self.request.GET.get('type')
        if q_word:
            object_list = Restaurant.objects.filter(
                Q(restaurant_name__icontains=q_word) | Q(certification__icontains=q_word)
            )
        elif q_data:
            object_list=Restaurant.objects.filter(
                Q(nearest_station__icontains=q_data)| Q(city__icontains=q_data)| Q(address1__icontains=q_data)
            )
        elif q_type:
            object_list=Restaurant.objects.filter(
                Q(restaurant_type__icontains=q_type)
            )
        else:
            object_list = Restaurant.objects.filter(prefectures="4")
        return object_list.filter(prefectures="4")


class RestaurantListHyogoView(LoginRequiredMixin,generic.ListView):
    """Hyogo"""
    model = Restaurant
    template_name = 'accountsDetail/restaurant_Hyogo.html'
    context_object_name = 'restaurant'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        q_type = self.request.GET.get('type')
        if q_word:
            object_list = Restaurant.objects.filter(
                Q(restaurant_name__icontains=q_word) | Q(certification__icontains=q_word)
            )
        elif q_data:
            object_list=Restaurant.objects.filter(
                Q(nearest_station__icontains=q_data)| Q(city__icontains=q_data)| Q(address1__icontains=q_data)
            )
        elif q_type:
            object_list=Restaurant.objects.filter(
                Q(restaurant_type__icontains=q_type)
            )
        else:
            object_list = Restaurant.objects.filter(prefectures="5")
        return object_list.filter(prefectures="5")


class RestaurantListNaraView(LoginRequiredMixin,generic.ListView):
    """Nara"""
    model = Restaurant
    template_name = 'accountsDetail/restaurant_Nara.html'
    context_object_name = 'restaurant'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        q_type = self.request.GET.get('type')
        if q_word:
            object_list = Restaurant.objects.filter(
                Q(restaurant_name__icontains=q_word) | Q(certification__icontains=q_word)
            )
        elif q_data:
            object_list=Restaurant.objects.filter(
                Q(nearest_station__icontains=q_data)| Q(city__icontains=q_data)| Q(address1__icontains=q_data)
            )
        elif q_type:
            object_list=Restaurant.objects.filter(
                Q(restaurant_type__icontains=q_type)
            )
        else:
            object_list = Restaurant.objects.filter(prefectures="6")
        return object_list.filter(prefectures="6")


class RestaurantListWakayamaView(LoginRequiredMixin,generic.ListView):
    """Wakayama"""
    model = Restaurant
    template_name = 'accountsDetail/restaurant_Wakayama.html'
    context_object_name = 'restaurant'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        q_type = self.request.GET.get('type')
        if q_word:
            object_list = Restaurant.objects.filter(
                Q(restaurant_name__icontains=q_word) | Q(certification__icontains=q_word)
            )
        elif q_data:
            object_list=Restaurant.objects.filter(
                Q(nearest_station__icontains=q_data)| Q(city__icontains=q_data)| Q(address1__icontains=q_data)
            )
        elif q_type:
            object_list=Restaurant.objects.filter(
                Q(restaurant_type__icontains=q_type)
            )
        else:
            object_list = Restaurant.objects.filter(prefectures="7")
        return object_list.filter(prefectures="7")

class RestaurantLinkView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'accountsDetail/restaurant_link.html'


class MyRestaurantDetailView(LoginRequiredMixin,generic.DetailView):
    model = User
    template_name = 'accountsDetail/my_restaurant_detail.html'
