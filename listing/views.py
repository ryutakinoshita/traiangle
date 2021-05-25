from django.shortcuts import redirect,render
from django.urls import reverse_lazy,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from listing.models import Listing
from django.http import HttpResponseRedirect
from listing.forms import ListingForm,ListingApplicationForm



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
    success_url = reverse_lazy('isting_application_finish')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)



class ListingApplicationFinishView(generic.TemplateView):
    template_name = 'listing/listing_application_finish.html'
