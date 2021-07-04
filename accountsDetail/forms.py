from django import forms
from .models import Restaurant, Review



class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = (
            "zip_code","prefectures","city","address1","address2","restaurant_name","restaurant_type","certification","restaurant_img1","restaurant_img2","restaurant_img3"
        )



class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = (
            "answer_text",
                  )