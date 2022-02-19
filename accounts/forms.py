from django import forms
from accounts.models import User
from django.contrib.auth.forms import(
UserCreationForm,
AuthenticationForm,
PasswordResetForm,
SetPasswordForm

)
from  django.forms import ModelForm
from django.core.mail import EmailMessage


class UserLoginForm(AuthenticationForm):
    """ログインフォーム"""
    class Meta:
        model = User
        fields = (
            'email', 'password',
        )
        labels = {
            'email': 'E-mail',
            'password': 'password',

        }


class UserCreateForm(UserCreationForm):
    """ユーザー登録フォーム"""
    class Meta:
        model = User
        exclude=(
            "rest_name",'restaurant_img1','restaurant_img2','restaurant_img3','certification',
            'nearest_station','business_hours_start','business_hours_end','business_hours_option',
            'restaurant_type',"zip_code","prefectures","city","address1","address2",'stripe_first_name_kana',
            'stripe_last_name_kana','stripe_state','stripe_city','stripe_town','stripe_line1','stripe_line2',
            'stripe_postal_code','stripe_state_kana','stripe_city_kana','stripe_town_kana','stripe_line1_kana',
            'stripe_line2_kana','stripe_day','stripe_month','stripe_year','stripe_gender','stripe_account_number',
            'stripe_bunk_code','stripe_routing_number','stripe_account_holder_name','stripe_img',
        )
        fields = (
            'first_name','last_name','email','phone','password1','password2','privacy_user','terms_user',
        )
        widgets = {
            'privacy_user': forms.CheckboxInput(),
            'terms_user': forms.CheckboxInput(),
        }



