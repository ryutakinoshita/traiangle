from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic
from django.core.signing import BadSignature, SignatureExpired, dumps, loads
from django.contrib.auth import get_user_model, login
from django.http import HttpResponseBadRequest
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,
)
from .forms import (
    UserLoginForm,
    UserCreateForm,
)

User = get_user_model()

class LoginView(LoginView):
    """ログイン機能"""
    form_class = UserLoginForm
    template_name = 'account/login.html'


class SignupView(generic.CreateView):
    """登録機能"""
    template_name = 'account/signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('signup_text')

    def form_valid(self,form):
        user = form.save()
        login(self.request, user,backend='django.contrib.auth.backends.ModelBackend')
        return super().form_valid(form)



class SignupTextView(generic.TemplateView):
    template_name = 'account/signup_text.html'

class SignupFinishView(generic.TemplateView):
    template_name = 'account/signup_finish.html'
