from listing.models import Listing
from django import forms
from django.core.mail import EmailMessage
from django.forms import ModelForm

class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = (
            "listing_img1","listing_img2","listing_img3","listing_type","listing_name","listing_text",
            "listing_price","consumption_time","sale"
                  )
        widgets={
            "sale":forms.RadioSelect()
        }



class ListingUpdateForm(ModelForm):

    class Meta:
        model = Listing
        fields = (
            "listing_type", "listing_name", "listing_text","listing_price","consumption_time","sale"
        )


