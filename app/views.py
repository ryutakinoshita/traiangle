from django.views import generic
from listing.models import Listing


class HomeView(generic.ListView):
    model = Listing
    template_name = 'app/home.html'
    context_object_name = 'Listings'

