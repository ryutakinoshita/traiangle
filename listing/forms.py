from listing.models import Listing
from django import forms



class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ("listing_img1","listing_img2","listing_img3","listing_type","listing_name","listing_text","listing_price")