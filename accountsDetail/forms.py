from django import forms
from .models import Producer,Restaurant, RestaurantImage

class ProducerForm(forms.ModelForm):

    class Meta:
        model = Producer
        fields = ("zip_code","prefectures_city","producer_type","certification","producer_img")


class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ("zip_code","prefectures","city","address1","address2",
                  "restaurant_name","restaurant_type","certification","restaurant_img")

class RestaurantImageForm(forms.ModelForm):

    class Meta:
        model = RestaurantImage
        fields = ("image_name1","restaurant_img1","image_name2","restaurant_img2","image_name3","restaurant_img3")

