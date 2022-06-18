from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect,render,get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from accounts.models import User
from django.conf import settings
from listing.models import Listing, Order, OrderItem, Payment
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import stripe
from django.shortcuts import resolve_url
from listing.forms import (
    ListingForm,
    ListingUpdateForm,
)




class ListingView(LoginRequiredMixin,generic.CreateView):
    """出品機能"""
    template_name = 'listing/listing_create.html'
    form_class = ListingForm
    success_url = reverse_lazy('my_page_restaurant')

    def form_valid(self, form):
        form.instance.listing_user =self.request.user
        return super().form_valid(form)


class ListingDetailView(LoginRequiredMixin,generic.DetailView):
    """商品詳細"""
    model = Listing
    template_name = 'listing/listing_detail.html'


class ListingUpdateView(LoginRequiredMixin,generic.UpdateView):
    """商品編集"""
    model = Listing
    form_class = ListingUpdateForm
    template_name = 'listing/listing_edit.html'

    def get_success_url(self):
        return resolve_url('my_page_restaurant')




class MyListingView(LoginRequiredMixin,generic.ListView):
    """自分の出品一覧"""
    model = Listing
    template_name = 'listing/my_listing.html'
    context_object_name = 'item_data'

    def get_queryset(self):
        return Listing.objects.filter(listing_user=self.request.user,status=1)



class OrderListView(LoginRequiredMixin,generic.ListView):
    """購入履歴"""
    model = OrderItem
    template_name = 'listing/order_list.html'
    context_object_name = 'item_data'

    def get_queryset(self):
        return OrderItem.objects.filter(user=self.request.user,item__status=1)




@login_required
def addItem(request, slug):
    """カートに追加"""
    item = get_object_or_404(Listing, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order = Order.objects.filter(user=request.user, ordered=False)

    if order.exists():
        order = order[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order = Order.objects.create(user=request.user, ordered_date=timezone.now())
        order.items.add(order_item)

    return redirect('order')


@login_required
def removeItem(request, slug):
    """商品の削除"""
    item = get_object_or_404(Listing, slug=slug)
    order = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order.exists():
        order = order[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            return redirect("order")

    return redirect("product", slug=slug)


@login_required
def removeSingleItem(request,slug):
    item = get_object_or_404(Listing, slug=slug)
    order = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order.exists():
        order = order[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
                order_item.delete()
            return redirect("order")

    return redirect("product", slug=slug)


class OrderView(LoginRequiredMixin,View):
    """商品決済確認"""
    def get(self,request,*args,**kwargs):
        try:
            order=Order.objects.get(user=request.user,ordered=False)
            context={
                'order':order
            }
            return render(request,'listing/order.html',context)
        except ObjectDoesNotExist:
            return render(request,'listing/order.html')



class ThanksView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'listing/thanks.html')





class PaymentView(LoginRequiredMixin, View):
    """商品決済完了"""
    def get(self, request, *args, **kwargs):
        order = Order.objects.get(user=request.user, ordered=False)
        user_data = User.objects.get(id=request.user.id)
        context = {
            'order': order,
            'user_data': user_data
        }
        return render(request, 'listing/payment.html', context)

    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        order = Order.objects.get(user=request.user, ordered=False)
        token = request.POST.get('stripeToken')
        amount = order.get_total()
        order_items = order.items.all()

        item_list = []
        for order_item in order_items:
            item_list.append(str(order_item.item) + '：' + str(order_item.quantity))
        description = ' '.join(item_list)

        charge = stripe.Charge.create(
            amount=amount,
            currency='jpy',
            description=description,
            source=token,
            stripe_account=order_item.item.listing_user.stripe_user_id,

        )

        payment = Payment(user=request.user)
        payment.stripe_charge_id = charge['id']
        payment.amount = amount
        payment.save()

        order_items.update(ordered=True)
        for item in order_items:
            item.save()

        order.ordered = True
        order.payment = payment
        order.save()

        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            "user":{
                "first_name":order_item.user.first_name,
                "last_name":order_item.user.last_name
            },
            "listing": {
                "listing_name": order_item.item.listing_name,
                "listing_price": order_item.item.listing_price,
                "listing_profit": order_item.item.listing_price * 0.964,
            }

        }

        subject="商品準備のお願い"
        message=render_to_string('listing/mails/order_subject.txt',context)
        from_email='triangle09best@gmail.com'
        recipient_list=[order_item.item.listing_user.email]
        send_mail(subject, message, from_email, recipient_list)
        return redirect('thanks')



class LikeBase(LoginRequiredMixin, View):
    """お気に入りベース"""
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        related_post = Listing.objects.get(pk=pk)

        if self.request.user in related_post.like.all():
            obj = related_post.like.remove(self.request.user)
        else:
            obj = related_post.like.add(self.request.user)
        return obj


class LikeHome(LikeBase):
    """ホームでページでお気に入りした場合"""
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return redirect('home')

class LikeDetail(LikeBase):
    """詳細ページでお気に入りした場合"""
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return redirect('home')




class BuyerListView(LoginRequiredMixin,generic.ListView):
    """購入者リスト"""
    model = OrderItem
    template_name = 'listing/buyer_list.html'
    context_object_name = 'item_data'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'item_data':OrderItem.objects.filter(item__listing_user=self.request.user),
            'order':Order.objects.all()


        })
        return context


class ConfirmedBase(LoginRequiredMixin, View):
    """確認ベース"""
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        confirmed_listing = OrderItem.objects.get(pk=pk)

        if self.request.user in confirmed_listing.confirmed.all():
            obj = confirmed_listing.confirmed.remove(self.request.user)
        else:
            obj = confirmed_listing.confirmed.add(self.request.user)
        return obj

class Confirmed(ConfirmedBase):
    """確認"""
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return redirect('buyer_list')



