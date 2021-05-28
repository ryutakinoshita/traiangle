from django.shortcuts import redirect,render,get_object_or_404
from django.urls import reverse_lazy,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from listing.models import Listing,Order,OrderItem
from django.http import HttpResponseRedirect
from listing.forms import ListingForm,ListingApplicationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist



class ListingView(generic.CreateView, LoginRequiredMixin):
    template_name = 'listing/listing_create.html'
    form_class = ListingForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.listing_user = self.request.user
        return super().form_valid(form)



class ListingApplicationView(generic.FormView):
    template_name = 'listing/listing_application.html'
    form_class =ListingApplicationForm
    success_url = reverse_lazy('listing_application_finish')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

@login_required
def addItem(request, slug):
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


class OrderView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        try:
            order=Order.objects.get(user=request.user,ordered=False)
            context={
                'order':order
            }
            return render(request,'listing/order.html',context)
        except ObjectDoesNotExist:
            return render(request,'listing/order.html')



class ListingApplicationFinishView(generic.TemplateView):
    template_name = 'listing/listing_application_finish.html'



class ListingDetailView(View):
    def get(self, request, *args, **kwargs):
        item_data = Listing.objects.get(slug=self.kwargs['slug'])
        return render(request, 'listing/listing_detail.html', {
            'item_data': item_data
        })