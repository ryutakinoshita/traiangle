from django import forms
from .models import Restaurant, Review
from django.core.mail import EmailMessage



class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = (
            'restaurant_name','restaurant_img1','restaurant_img2','restaurant_img3','restaurant_type','zip_code','prefectures','city','address1','address2',
            'certification','nearest_station','business_hours_start','business_hours_end','business_hours_option'

        )
        widgets = {
            'restaurant_type': forms.RadioSelect(),
            'business_hours_option': forms.RadioSelect(),
            'business_hours_start': forms.TimeInput(format='%H:%M'),
            'business_hours_end': forms.TimeInput(format='%H:%M'),

        }



class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = (
            "answer_text",
                  )



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
                               to=[""],
                               cc=[email])
        message.send()