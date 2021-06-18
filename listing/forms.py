from listing.models import Listing
from django import forms
from django.core.mail import EmailMessage
from django.forms import ModelForm

class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = ("listing_img1","listing_img2","listing_img3","listing_type","listing_name","listing_text","listing_price")

class ListingUpdateForm(ModelForm):

    class Meta:
        model = Listing
        fields = (
        "listing_img1", "listing_img2", "listing_img3", "listing_type", "listing_name", "listing_text", "listing_price")


# class ListingApplicationForm(forms.Form):
#     CHOICE=(
#         ("1", "野菜"),
#         ("2", "果物"),
#         ("3", "鮮魚"),
#         ("4", "食肉"),
#         ("5", "乳製品"),
#         ("6", "加工食品"),
#         ("7", "飲料"),
#         ("9", "アルコール飲料"),
#         ("10", "園芸"),
#         ("11", "その他"),
#     )
#     producer_name=forms.CharField(max_length=30)
#     email=forms.EmailField()
#     zip_code = forms.CharField(max_length=8)
#     prefectures_city=forms.CharField(max_length=40)
#     producer_type = forms.TypedChoiceField(choices=CHOICE)
#     text = forms.CharField(max_length=500,widget=forms.Textarea)
#
#     def send_email(self):
#         producer_name = self.cleaned_data['producer_name']
#         email = self.cleaned_data['email']
#         zip_code = self.cleaned_data['zip_code']
#         prefectures_city = self.cleaned_data['prefectures_city']
#         producer_type  = self.cleaned_data['producer_type ']
#         text = self.cleaned_data['text']
#
#
#         message = EmailMessage(subject=producer_name + "からの登録申請",
#                                body="生産地:"+"〒"+zip_code+prefectures_city+"申請内容:"+text+producer_type,
#                                from_email=email,
#                                to=[""],
#                                cc=[email])
#         message.send()
