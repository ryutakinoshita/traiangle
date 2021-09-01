from django import forms
from django.core.mail import EmailMessage



class RefundForm(forms.Form):

    rest_name=forms.CharField(max_length=30)
    email=forms.EmailField()
    listing_name=forms.CharField(max_length=30)
    price=forms.IntegerField()
    date=forms.DateField()
    buyer=forms.CharField(max_length=30)
    text = forms.CharField(max_length=500,widget=forms.Textarea)

    def send_email(self):
        rest_name = self.cleaned_data['rest_name']
        email = self.cleaned_data['email']
        text = self.cleaned_data['text']
        listing_name = self.cleaned_data['listing_name']
        price = self.cleaned_data['price']
        buyer = self.cleaned_data['buyer']
        date = self.cleaned_data['date']



        message = EmailMessage(subject=rest_name + "からの返金依頼",
                               body="お客様名:"+buyer+"E-mail"+email+"商品名:"+listing_name+"価格:"+"￥:"+price+"購入日"+date+"備考"+text,
                               from_email="ryuta05590531@gmail.com",
                               to=["triangle09best@gmail.com"],
                               cc=[email])
        message.send()


