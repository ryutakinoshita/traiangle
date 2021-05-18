from django import forms
from .models import Individual,Producer,Restaurant


class IndividualForm(forms.ModelForm):

    class Meta:
        model = Individual
        fields = ("zip_code","prefectures","city","address1","address2")


class ProducerForm(forms.ModelForm):

    class Meta:
        model = Producer
        fields = ("zip_code","prefectures_city","producer_name","producer_type","certification","producer_img")
        widgets = {
            'producer_type': forms.CheckboxSelectMultiple(),
        }

class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ("zip_code","prefectures","city","address1","address2",
                  "restaurant_name","restaurant_type","certification","restaurant_img")
        widgets = {
            'producer_type': forms.RadioSelect(),
            "restaurant_img":forms.ClearableFileInput(attrs={'multiple': True})
        }

