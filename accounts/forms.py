from django.forms import ModelForm,forms
from accounts.models import User
from django.contrib.auth.forms import(
UserCreationForm,
AuthenticationForm,

)



class UserLoginForm(AuthenticationForm):
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
    class Meta:
        model = User
        fields = [
            'first_name','last_name','email','phone','password1', 'password2',
        ]

