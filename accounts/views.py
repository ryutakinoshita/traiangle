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
    PasswordResetCompleteView,
)
from .forms import (
    UserLoginForm,
    UserCreateForm,
    EmailChangeForm,
    PasswordResetForm,
    SetPasswordForm,
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

        return redirect('email_change_done')


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