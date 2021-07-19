from django import forms
from django.core.mail import EmailMessage





class ApplicationForm(forms.Form):
    Types=(
        ("1", "食堂，レストラン"),
        ("2", "日本料理店"),
        ("3", "料亭"),
        ("4", "中華料理店"),
        ("5", "ラーメン店"),
        ("6", "焼肉店"),
        ("7", "そば・うどん店"),
        ("8", "酒場、ビヤホール"),
        ("9", "喫茶店"),
        ("10", "その他の飲食店"),
        ("11", "ハンバーガー店"),
        ("12", "イタリア料理店"),
        ("13", "アジア料理店"),
    )

    restaurant_name=forms.CharField(max_length=30)
    email=forms.EmailField()
    text = forms.CharField(max_length=500,widget=forms.Textarea)
    zip_code = forms.CharField(max_length=8)
    prefectures=forms.CharField(max_length=40)
    city = forms.CharField(max_length=40)
    address1 = forms.CharField(max_length=40)
    address2 = forms.CharField(max_length=40)
    nearest_station = forms.CharField(max_length=40)
    restaurant_type = forms.ChoiceField(choices=Types,widget=forms.RadioSelect)

    def send_email(self):
        restaurant_name = self.cleaned_data['restaurant_name']
        email = self.cleaned_data['email']
        zip_code = self.cleaned_data['zip_code']
        prefectures = self.cleaned_data['prefectures']
        city = self.cleaned_data['city']
        address1 = self.cleaned_data['address1']
        address2 = self.cleaned_data['address2']
        nearest_station = self.cleaned_data['nearest_station']
        restaurant_type  = self.cleaned_data['restaurant_type']
        text = self.cleaned_data['text']


        message = EmailMessage(subject=restaurant_name + "からの出店申請",
                               body="店舗住所:"+"〒"+zip_code+prefectures+city+address1+address2+"最寄り駅:"+nearest_station+"申請内容:"+text+restaurant_type,
                               from_email=email,
                               to=["kinoshitaryuta@gmail.com"],
                               cc=[email])
        message.send()


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
                               body="お客様名:"+buyer+"商品名:"+listing_name+"価格:"+"￥:"+price+"購入日"+date+"備考"+text,
                               from_email=email,
                               to=["kinoshitaryuta@gmail.com"],
                               cc=[email])
        message.send()