from django.shortcuts import redirect,render
from django.urls import reverse_lazy,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from listing.forms import ListingForm
from listing.models import Listing
from django.http import HttpResponseRedirect



class ListingView(generic.CreateView, LoginRequiredMixin):
    template_name = 'listing/listing_create.html'
    form_class = ListingForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)






class ListingApplicationView(generic.TemplateView):
    template_name = 'listing/listing_application.html'





