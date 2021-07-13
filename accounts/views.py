from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic
from django.core.signing import BadSignature, SignatureExpired, dumps, loads
from django.contrib.auth import get_user_model, login
from django.http import HttpResponseBadRequest
from django.conf import settings
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
)
from .forms import (
    UserLoginForm,
    UserCreateForm,
    EmailChangeForm,
    PasswordResetForm,
    SetPasswordForm,
    UserZipUpdateForm,
    RestaurantUserCreateForm,
    RestaurantUserUpdateForm,
)
from django.shortcuts import resolve_url


User = get_user_model()

class LoginView(LoginView):
    """ログイン機能"""
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get_success_url(self):
        return resolve_url('home')


class SignupView(generic.CreateView):
    """登録機能"""
    template_name = 'account/signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """仮登録と本登録用メールの発行"""
        user = form.save(commit=False)
        user.is_active = False
        user.save()


        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject = render_to_string('account/mails/user_create_subject.txt', context)
        message = render_to_string('account/mails/user_create_message.txt', context)

        user.email_user(subject, message)
        return redirect('user_create_done')


class SignupDoneView(generic.TemplateView):
    template_name = 'account/sign_up_done.html'


class SignupFinishView(generic.TemplateView):
    template_name = 'account/signup_finish.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60 * 60 * 24)


    def get(self, request, **kwargs):
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)
        except SignatureExpired:
            return HttpResponseBadRequest()

        except BadSignature:
            return HttpResponseBadRequest()

        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    # 問題なければ本登録とする
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()


class RestaurantLoginView(LoginView):
    """レストランログイン機能"""
    form_class = UserLoginForm
    template_name = 'account/restaurant_login.html'

    def get_success_url(self):
        return resolve_url('my_page_restaurant')

class RestaurantUserCreateView(generic.CreateView):
    """レストランユーザー登録機能"""
    template_name = 'account/restaurant_signup.html'
    form_class = RestaurantUserCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """仮登録と本登録用メールの発行"""
        user = form.save(commit=False)
        user.is_active = False
        user.save()


        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,
            'token': dumps(user.pk),
            'user': user,
        }

        subject = render_to_string('account/mails/restaurant_create_subject.txt', context)
        message = render_to_string('account/mails/restaurant_create_message.txt', context)

        user.email_user(subject, message)
        return redirect('user_create_done')

class RestaurantFinishView(generic.TemplateView):
    template_name = 'account/restaurant_finish.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60 * 60 * 24)

    def get(self, request, **kwargs):
        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)
        except SignatureExpired:
            return HttpResponseBadRequest()

        except BadSignature:
            return HttpResponseBadRequest()

        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    # 問題なければ本登録とする
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()


class EmailChangeView(LoginRequiredMixin, generic.FormView):
    """メールアドレスの変更"""
    template_name = 'account/email_change_form.html'
    form_class = EmailChangeForm

    def form_valid(self, form):
        user = self.request.user
        new_email = form.cleaned_data['email']

        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': 'https' if self.request.is_secure() else 'http',
            'domain': domain,
            'token': dumps(new_email),
            'user': user,
        }

        subject = render_to_string('account/mails/E-mail_change_subject.txt', context)
        message = render_to_string('account/mails/E-mail_change_message.txt', context)
        send_mail(subject, message, None, [new_email])

        return redirect('user_create_done')


class EmailChangeDoneView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'account/email_change_done.html'


class EmailChangeCompleteView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'account/email_change_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)

    def get(self, request, **kwargs):
        token = kwargs.get('token')
        try:
            new_email = loads(token, max_age=self.timeout_seconds)

        except SignatureExpired:
            return HttpResponseBadRequest()

        except BadSignature:
            return HttpResponseBadRequest()

        else:
            User.objects.filter(email=new_email, is_active=False).delete()
            request.user.email = new_email
            request.user.save()
            return super().get(request, **kwargs)


class PasswordResetView(PasswordResetView):
    """パスワード再設定"""
    subject_template_name = 'account/mails/password_reset_subject.txt'
    email_template_name = 'account/mails/password_reset_message.txt'
    template_name = 'account/password_reset_form.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')


class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class PasswordResetConfirmView(PasswordResetConfirmView):
    """新パスワード入力ページ"""
    form_class = SetPasswordForm
    success_url = reverse_lazy('password_done')
    template_name = 'account/password_reset_confirm.html'


class PasswordDoneView(generic.TemplateView):
    template_name = 'account/password_done.html'


class UserZipUpdateView(generic.UpdateView):
    """住所変更"""
    model = User
    form_class = UserZipUpdateForm
    template_name = 'account/user_edit.html'

    def get_success_url(self):
        return resolve_url('my_page')

class RestaurantUserUpdateView(generic.UpdateView):
    """レストラン情報変更"""
    model = User
    form_class = RestaurantUserUpdateForm
    template_name = 'account/restaurant_edit.html'

    def get_success_url(self):
        return resolve_url('my_page_restaurant')

