from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic
from django.core.signing import BadSignature, SignatureExpired, dumps, loads
from django.contrib.auth import get_user_model, login
from django.http import HttpResponseBadRequest
from django.conf import settings
from django.shortcuts import resolve_url
import stripe

from django.contrib.auth.views import (
    LoginView,
)
from .forms import (
    UserLoginForm,
    UserCreateForm,
)
User = get_user_model()
stripe.api_key = settings.STRIPE_SECRET_KEY



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
                    user.is_active = True
                    user.save()
                    return super().get(request, **kwargs)

        return HttpResponseBadRequest()


class RestaurantLoginView(LoginView):
    """レストランログイン機能"""
    form_class = UserLoginForm
    template_name = 'account/restaurant_login.html'

    def get_success_url(self):
        current_site = get_current_site(self.request)
        domain = current_site.domain
        context = {
            'protocol': self.request.scheme,
            'domain': domain,

        }

        subject = "新規登録がありました"
        message = render_to_string('account/mails/new_user_subject.txt', context)
        from_email = 'triangle09best@gmail.com'
        recipient_list = ['kinoshitaryuta@gmail.com']
        send_mail(subject, message, from_email, recipient_list)
        return resolve_url('application_done')





