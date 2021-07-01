from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from app.forms import ContactForm
from app.models import Withdrawal
from listing.models import Listing
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.db.models import Q
from django.utils import timezone



class HomeView(generic.ListView):
    """ホーム"""
    model = Listing
    template_name = 'app/home.html'
    context_object_name = 'item_data'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['likes'] = Listing.objects.order_by('like')
        return context


class ProductListView(LoginRequiredMixin,generic.ListView):
    """商品一覧"""
    model = Listing
    template_name = 'app/product.html'
    context_object_name = 'product'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) | Q(listing_text__icontains=q_word)
            )
        else:
            object_list = Listing.objects.order_by('?')
        return object_list


class ProductListVegetablesView(LoginRequiredMixin,generic.ListView):
    """野菜一覧"""
    model = Listing
    template_name = 'app/product_vegetables.html'
    context_object_name = 'product'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) | Q(listing_text__icontains=q_word)
            )
        else:
            object_list = Listing.objects.filter(listing_type="1")
        return object_list.filter(listing_type="1")


class ProductListFruitsView(LoginRequiredMixin,generic.ListView):
    """果物一覧"""
    model = Listing
    template_name = 'app/product_fruits.html'
    context_object_name = 'product'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) | Q(listing_text__icontains=q_word)
            )
        else:
            object_list = Listing.objects.filter(listing_type="2")
        return object_list.filter(listing_type="2")


class ProductListFishView(LoginRequiredMixin,generic.ListView):
    """鮮魚一覧"""
    model = Listing
    template_name = 'app/product_fish.html'
    context_object_name = 'product'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) | Q(listing_text__icontains=q_word)
            )
        else:
            object_list = Listing.objects.filter(listing_type="3")
        return object_list.filter(listing_type="3")


class ProductListMeatView(LoginRequiredMixin,generic.ListView):
    """食肉一覧"""
    model = Listing
    template_name = 'app/product_meat.html'
    context_object_name = 'product'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) | Q(listing_text__icontains=q_word)
            )
        else:
            object_list = Listing.objects.filter(listing_type="4")
        return object_list.filter(listing_type="4")


class ProductListDairyView(LoginRequiredMixin,generic.ListView):
    """乳製品一覧"""
    model = Listing
    template_name = 'app/product_dairy.html'
    context_object_name = 'product'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) | Q(listing_text__icontains=q_word)
            )
        else:
            object_list = Listing.objects.filter(listing_type="5")
        return object_list.filter(listing_type="5")


class ProductListProcessingView(LoginRequiredMixin,generic.ListView):
    """加工食品"""
    model = Listing
    template_name = 'app/product_processing.html'
    context_object_name = 'product'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) | Q(listing_text__icontains=q_word)
            )
        else:
            object_list = Listing.objects.filter(listing_type="6")
        return object_list.filter(listing_type="6")


class ProductListDrinkView(LoginRequiredMixin,generic.ListView):
    """飲料"""
    model = Listing
    template_name = 'app/product_drink.html'
    context_object_name = 'product'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) | Q(listing_text__icontains=q_word)
            )
        else:
            object_list = Listing.objects.filter(listing_type="7")
        return object_list.filter(listing_type="7")


class ProductListAlcoholView(LoginRequiredMixin,generic.ListView):
    """アルコール飲料"""
    model = Listing
    template_name = 'app/product_alcohol.html'
    context_object_name = 'product'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) | Q(listing_text__icontains=q_word)
            )
        else:
            object_list = Listing.objects.filter(listing_type="8")
        return object_list.filter(listing_type="8")


class ProductListOtherView(LoginRequiredMixin,generic.ListView):
    """"その他"""
    model = Listing
    template_name = 'app/product_other.html'
    context_object_name = 'product'

    # 検索
    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = Listing.objects.filter(
                Q(listing_name__icontains=q_word) | Q(listing_text__icontains=q_word)
            )
        else:
            object_list = Listing.objects.filter(listing_type="9")
        return object_list.filter(listing_type="9")


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
                success_url=domain_url + 'account/signup',
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

