from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.db.models import Q
from accounts.models import User
from listing.models import Listing
from .forms import (
    RefundForm,
)


class MyPageView(LoginRequiredMixin,generic.TemplateView):
    """マイページ"""
    template_name = 'accountsDetail/my_page.html'


class MyPageDetailView(LoginRequiredMixin,generic.DetailView):
    """ユーザー情報確認"""
    model = User
    template_name = 'accountsDetail/my_page_detail.html'



class ApplicationDoneView(generic.TemplateView):
    template_name = 'accountsDetail/application_done.html'


class RefundView(FormView):
    """返金申請"""
    template_name = 'accountsDetail/Refund.html'
    form_class = RefundForm
    success_url = reverse_lazy('refund_done')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

class RefundDoneView(generic.TemplateView):
    template_name = 'accountsDetail/Refund_done.html'


class RestaurantMyPageView(LoginRequiredMixin,generic.TemplateView):
    """レストランマイページ"""
    template_name = 'accountsDetail/my_page_restaurant.html'


class RestaurantDetailView(LoginRequiredMixin,generic.DetailView):
    """レストラン詳細"""
    model = User
    template_name = 'accountsDetail/restaurant_detail.html'
    context_object_name = 'restaurants'


class RestaurantListMieView(LoginRequiredMixin,generic.ListView):
    """Mie"""
    model = User
    template_name = 'accountsDetail/restaurant_Mie.html'
    context_object_name = 'restaurant'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        q_type = self.request.GET.get('type')
        if q_word:
            object_list = User.objects.filter(
                Q(rest_name__icontains=q_word) | Q(certification__icontains=q_word)
            )
        elif q_data:
            object_list=User.objects.filter(
                Q(nearest_station__icontains=q_data)| Q(city__icontains=q_data)| Q(address1__icontains=q_data)
            )
        elif q_type:
            object_list=User.objects.filter(
                Q(restaurant_type__icontains=q_type)
            )
        else:
            object_list = User.objects.filter(prefectures="1")
        return object_list.filter(prefectures="1")


class RestaurantListSigaView(LoginRequiredMixin,generic.ListView):
    """Siga"""
    model = User
    template_name = 'accountsdetail/restaurant_Siga.html'
    context_object_name = 'restaurant'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        q_type = self.request.GET.get('type')
        if q_word:
            object_list = User.objects.filter(
                Q(rest_name__icontains=q_word) | Q(certification__icontains=q_word)
            )
        elif q_data:
            object_list=User.objects.filter(
                Q(nearest_station__icontains=q_data)| Q(city__icontains=q_data)| Q(address1__icontains=q_data)
            )
        elif q_type:
            object_list=User.objects.filter(
                Q(restaurant_type__icontains=q_type)
            )
        else:
            object_list = User.objects.filter(prefectures="2")
        return object_list.filter(prefectures="2")


class RestaurantListKyotoView(LoginRequiredMixin,generic.ListView):
    """Kyoto"""
    model = User
    template_name = 'accountsdetail/restaurant_Kyoto.html'
    context_object_name = 'restaurant'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        q_type = self.request.GET.get('type')
        if q_word:
            object_list = User.objects.filter(
                Q(rest_name__icontains=q_word) | Q(certification__icontains=q_word)
            )
        elif q_data:
            object_list = User.objects.filter(
                Q(nearest_station__icontains=q_data) | Q(city__icontains=q_data) | Q(address1__icontains=q_data)
            )
        elif q_type:
            object_list = User.objects.filter(
                Q(restaurant_type__icontains=q_type)
            )
        else:
            object_list = User.objects.filter(prefectures="3")
        return object_list.filter(prefectures="3")


class RestaurantListOsakaView(LoginRequiredMixin,generic.ListView):
    """Osaka"""
    model = User
    template_name = 'accountsdetail/restaurant_Osaka.html'
    context_object_name = 'restaurant'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        q_type = self.request.GET.get('type')
        if q_word:
            object_list = User.objects.filter(
                Q(rest_name__icontains=q_word) | Q(certification__icontains=q_word)
            )
        elif q_data:
            object_list = User.objects.filter(
                Q(nearest_station__icontains=q_data) | Q(city__icontains=q_data) | Q(address1__icontains=q_data)
            )
        elif q_type:
            object_list = User.objects.filter(
                Q(restaurant_type__icontains=q_type)
            )
        else:
            object_list = User.objects.filter(prefectures="4")
        return object_list.filter(prefectures="4")


class RestaurantListHyogoView(LoginRequiredMixin,generic.ListView):
    """Hyogo"""
    model = User
    template_name = 'accountsdetail/restaurant_Hyogo.html'
    context_object_name = 'restaurant'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        q_type = self.request.GET.get('type')
        if q_word:
            object_list = User.objects.filter(
                Q(rest_name__icontains=q_word) | Q(certification__icontains=q_word)
            )
        elif q_data:
            object_list = User.objects.filter(
                Q(nearest_station__icontains=q_data) | Q(city__icontains=q_data) | Q(address1__icontains=q_data)
            )
        elif q_type:
            object_list = User.objects.filter(
                Q(restaurant_type__icontains=q_type)
            )
        else:
            object_list = User.objects.filter(prefectures="5")
        return object_list.filter(prefectures="5")

class RestaurantListNaraView(LoginRequiredMixin,generic.ListView):
    """Nara"""
    model = User
    template_name = 'accountsdetail/restaurant_Nara.html'
    context_object_name = 'restaurant'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        q_type = self.request.GET.get('type')
        if q_word:
            object_list = User.objects.filter(
                Q(rest_name__icontains=q_word) | Q(certification__icontains=q_word)
            )
        elif q_data:
            object_list=User.objects.filter(
                Q(nearest_station__icontains=q_data)| Q(city__icontains=q_data)| Q(address1__icontains=q_data)
            )
        elif q_type:
            object_list=User.objects.filter(
                Q(restaurant_type__icontains=q_type)
            )
        else:
            object_list = User.objects.filter(prefectures="6")
        return object_list.filter(prefectures="6")


class RestaurantListWakayamaView(LoginRequiredMixin,generic.ListView):
    """Wakayama"""
    model = User
    template_name = 'accountsdetail/restaurant_Wakayama.html'
    context_object_name = 'restaurant'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        q_type = self.request.GET.get('type')
        if q_word:
            object_list = User.objects.filter(
                Q(rest_name__icontains=q_word) | Q(certification__icontains=q_word)
            )
        elif q_data:
            object_list = User.objects.filter(
                Q(nearest_station__icontains=q_data) | Q(city__icontains=q_data) | Q(address1__icontains=q_data)
            )
        elif q_type:
            object_list = User.objects.filter(
                Q(restaurant_type__icontains=q_type)
            )
        else:
            object_list = User.objects.filter(prefectures="7")
        return object_list.filter(prefectures="7")


class RestaurantLinkView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'accountsdetail/restaurant_link.html'

class MyRestaurantDetailView(LoginRequiredMixin,generic.DetailView):
    model = User
    template_name = 'accountsdetail/my_restaurant_detail.html'
