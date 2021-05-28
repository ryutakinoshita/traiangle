from django.views import generic
from django.shortcuts import render
from django.views.generic import View
from listing.models import Listing



class HomeView(View):
    def get(self, request, *args, **kwargs):
        item_data = Listing.objects.all()
        return render(request, 'app/home.html', {
            'item_data': item_data
        })