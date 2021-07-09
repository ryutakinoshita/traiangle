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
        fields = [
            'email', 'password',
        ]
        labels = {
            'email': 'E-mail',
            'password': 'password',

        }

class UserCreateForm(UserCreationForm):
    """全ユーザー登録フォーム"""
    class Meta:
        model = User
        exclude=(
            "rest_name",
        )
        fields = [
            'first_name','last_name','email','phone','password1','password2',"zip_code","prefectures","city",
            "address1","address2",
        ]
class RestaurantUserCreateForm(UserCreationForm):
    """レストランユーザー登録フォーム"""
    class Meta:
        model = User
        fields = [
            'first_name','last_name','email','phone','password1','password2',"zip_code","prefectures","city",
            "address1","address2","rest_name",
        ]

class EmailChangeForm(forms.ModelForm):
    """メールアドレス変更"""
    class Meta:
        model = User
        fields = [
            'email',
        ]

    def clean_email(self):
        email = self.cleaned_data['email']
        User.objects.filter(email=email, is_active=False).delete()
        return email


class PasswordResetForm(PasswordResetForm):
    """パスワードの再設定"""
    class Meta:
        model = User
        fields = [
            'email',
        ]


class SetPasswordForm(SetPasswordForm):
    """新パスワードの設定"""
    class Meta:
        model = User
        fields = [
            'password1','password2'
        ]


class UserZipUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "zip_code", "prefectures", "city","address1", "address2",
        ]

