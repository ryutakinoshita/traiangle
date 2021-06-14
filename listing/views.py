from django.shortcuts import redirect,render,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from accounts.models import User
from django.conf import settings
from listing.models import Listing, Order, OrderItem, Payment
from listing.forms import ListingForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import stripe



class ListingView(generic.CreateView,LoginRequiredMixin):
    """出品機能"""
    template_name = 'listing/listing_create.html'
    form_class = ListingForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.listing_user = self.request.user
        return super().form_valid(form)



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
def removeSingleItem(request, slug):
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


class ListingDetailView(generic.DetailView):
    model = Listing
    template_name = 'listing/listing_detail.html'


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
        return redirect('thanks')


class OrderListView(generic.ListView):
    """購入履歴"""
    template_name = 'listing/order_list.html'
    model = OrderItem
    context_object_name = 'orders'

