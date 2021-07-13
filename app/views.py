from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from accounts.models import User
from app.forms import ContactForm
from app.models import Withdrawal
from listing.models import Listing
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.db.models import Q
from django.utils import timezone
from recipe.models import Recipe


class HomeView(generic.ListView):
    """ホーム"""
    model = Listing
    template_name = 'app/home.html'
    context_object_name = 'item_data'



    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'likes':Listing.objects.order_by('like'),
            'good':Recipe.objects.order_by('good'),
            'restaurants':User.objects.all(),
        })
        return context

class ProductListView(LoginRequiredMixin,generic.ListView):
    """商品一覧"""
    model = Listing
    template_name = 'app/product.html'
    context_object_name = 'item_data'



    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')

        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) |
                Q(listing_text__icontains=q_word) |
                Q(listing_user__city__icontains=q_word) |
                Q(listing_user__address1__icontains=q_word) |
                Q(listing_user__rest_name__icontains=q_word)
            )
        elif q_data:
            object_list = Listing.objects.filter(
                Q(listing_price__lte=q_data)
            )
        else:
            object_list = Listing.objects.order_by('?')
        return object_list

class ProductListMieView(LoginRequiredMixin,generic.ListView):
    """Mie"""
    model = Listing
    template_name = 'app/listing_Mie.html'
    context_object_name = 'item_data'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word)|
                Q(listing_text__icontains=q_word)|
                Q(listing_user__city__icontains=q_word)|
                Q(listing_user__address1__icontains=q_word)|
                Q(listing_user__rest_name__icontains=q_word)
            )
        elif q_data:
            object_list = Listing.objects.filter(

            )
        else:
            object_list = Listing.objects.filter(listing_user__prefectures__icontains="1")
        return object_list.filter(listing_user__prefectures__icontains="1")


class ProductListSigaView(LoginRequiredMixin,generic.ListView):
    """Siga"""
    model = Listing
    template_name = 'app/listing_Siga.html'
    context_object_name = 'item_data'


    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) |
                Q(listing_text__icontains=q_word) |
                Q(listing_user__city__icontains=q_word) |
                Q(listing_user__address1__icontains=q_word) |
                Q(listing_user__rest_name__icontains=q_word)
            )
        elif q_data:
            object_list = Listing.objects.filter(

            )
        else:
            object_list = Listing.objects.filter(listing_user__prefectures__icontains="2")
        return object_list.filter(listing_user__prefectures__icontains="2")


class ProductListKyotoView(LoginRequiredMixin,generic.ListView):
    """Kyoto"""
    model = Listing
    template_name = 'app/listing_Kyoto.html'
    context_object_name = 'item_data'


    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) |
                Q(listing_text__icontains=q_word) |
                Q(listing_user__city__icontains=q_word) |
                Q(listing_user__address1__icontains=q_word) |
                Q(listing_user__rest_name__icontains=q_word)
            )
        elif q_data:
            object_list = Listing.objects.filter(

            )
        else:
            object_list = Listing.objects.filter(listing_user__prefectures__icontains="3")
        return object_list.filter(listing_user__prefectures__icontains="3")


class ProductListOsakaView(LoginRequiredMixin,generic.ListView):
    """Osaka"""
    model = Listing
    template_name = 'app/listing_Osaka.html'
    context_object_name = 'item_data'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) |
                Q(listing_text__icontains=q_word) |
                Q(listing_user__city__icontains=q_word) |
                Q(listing_user__address1__icontains=q_word) |
                Q(listing_user__rest_name__icontains=q_word)
            )
        elif q_data:
            object_list = Listing.objects.filter(

            )
        else:
            object_list = Listing.objects.filter(listing_user__prefectures__icontains="4")
        return object_list.filter(listing_user__prefectures__icontains="4")


class ProductListHyogoView(LoginRequiredMixin,generic.ListView):
    """Hyogo"""
    model = Listing
    template_name = 'app/listing_Hyogo.html'
    context_object_name = 'item_data'


    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) |
                Q(listing_text__icontains=q_word) |
                Q(listing_user__city__icontains=q_word) |
                Q(listing_user__address1__icontains=q_word) |
                Q(listing_user__rest_name__icontains=q_word)
            )
        elif q_data:
            object_list = Listing.objects.filter(

            )
        else:
            object_list = Listing.objects.filter(listing_user__prefectures__icontains="5")
        return object_list.filter(listing_user__prefectures__icontains="5")


class ProductListNaraView(LoginRequiredMixin,generic.ListView):
    """Nara"""
    model = Listing
    template_name = 'app/listing_Nara.html'
    context_object_name = 'item_data'


    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) |
                Q(listing_text__icontains=q_word) |
                Q(listing_user__city__icontains=q_word) |
                Q(listing_user__address1__icontains=q_word) |
                Q(listing_user__rest_name__icontains=q_word)
            )
        elif q_data:
            object_list = Listing.objects.filter(

            )
        else:
            object_list = Listing.objects.filter(listing_user__prefectures__icontains="6")
        return object_list.filter(listing_user__prefectures__icontains="6")


class ProductListWakayamaView(LoginRequiredMixin,generic.ListView):
    """Wakayama"""
    model = Listing
    template_name = 'app/listing_Wakayama.html'
    context_object_name = 'item_data'


    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        q_data = self.request.GET.get('data')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) |
                Q(listing_text__icontains=q_word) |
                Q(listing_user__city__icontains=q_word) |
                Q(listing_user__address1__icontains=q_word) |
                Q(listing_user__rest_name__icontains=q_word)
            )
        elif q_data:
            object_list=Listing.objects.filter(

            )
        else:
            object_list = Listing.objects.filter(listing_user__prefectures__icontains="7")
        return object_list.filter(listing_user__prefectures__icontains="7")


class AppView(generic.TemplateView):
    template_name = 'app/app.html'


def index(request):
    """サブスクリプションページ"""
    return render(request, 'app/index.html')


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    """サブスクリプション"""
    if request.method == 'GET':
        domain_url = 'http://127.0.0.1:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'account/signup/restaurant/',
                cancel_url=domain_url + 'cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

def cancel(request):
    """決済できなかった場合"""
    return render(request, 'app/cancel.html')


class ContactView(LoginRequiredMixin,generic.CreateView):
    template_name = 'app/contact_form.html'
    model = Withdrawal
    form_class = ContactForm
    success_url = reverse_lazy('contact_result')

    def form_valid(self, form):
        form.instance.user = self.request.user
        subject="退会申請"
        message="退会申請がありました。"
        from_email=self.request.user.email
        recipient_list=["information@myproject"]
        send_mail(subject, message, from_email, recipient_list)
        return super().form_valid(form)




class ContactResultView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'app/contact_result.html'

