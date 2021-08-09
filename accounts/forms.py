from django import forms
from accounts.models import User
from django.contrib.auth.forms import(
UserCreationForm,
AuthenticationForm,
PasswordResetForm,
SetPasswordForm

)
from  django.forms import ModelForm


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
            'stripe_line2_kana','stripe_day','stripe_month','stripe_year','stripe_gender',
        )
        fields = (
            'first_name','last_name','email','phone','password1','password2','privacy_user','terms_user',
        )
        widgets = {
            'privacy_user': forms.CheckboxInput(),
            'terms_user': forms.CheckboxInput(),
        }



class RestaurantUserCreateForm(UserCreationForm):
    """レストランユーザー登録フォーム"""
    class Meta:
        model = User
        fields = (
            'first_name','last_name','email','phone','password1','password2',"zip_code","prefectures","city",
            "address1","address2","rest_name",'restaurant_img1','restaurant_img2','restaurant_img3','certification',
            'nearest_station','business_hours_start','business_hours_end','business_hours_option','restaurant_type',
            'privacy_user','terms_user','stripe_first_name_kana','stripe_last_name_kana','stripe_state','stripe_city',
            'stripe_town','stripe_line1','stripe_line2','stripe_postal_code','stripe_state_kana','stripe_city_kana',
            'stripe_town_kana','stripe_line1_kana','stripe_line2_kana','stripe_day','stripe_month','stripe_year','stripe_gender',

        )
        widgets = {
            'privacy_user': forms.CheckboxInput(),
            'terms_user': forms.CheckboxInput(),
        }


class EmailChangeForm(forms.ModelForm):
    """メールアドレス変更"""
    class Meta:
        model = User
        fields = (
            'email',
        )

    def clean_email(self):
        email = self.cleaned_data['email']
        User.objects.filter(email=email, is_active=False).delete()
        return email


class PasswordResetForm(PasswordResetForm):
    """パスワードの再設定"""
    class Meta:
        model = User
        fields = (
            'email',
        )


class SetPasswordForm(SetPasswordForm):
    """新パスワードの設定"""
    class Meta:
        model = User
        fields = (
            'password1','password2'
        )


class RestaurantUserUpdateForm(ModelForm):
    """レストラン変更フォーム"""
    class Meta:
        model = User
        fields = (
            'phone',"zip_code","prefectures","city",
            "address1","address2","rest_name",'certification',
            'nearest_station','business_hours_start','business_hours_end','business_hours_option','restaurant_type'
        )