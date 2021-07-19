from django.forms import ModelForm
from app.models import Withdrawal
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse




class ContactForm(ModelForm):
    class Meta:
        model = Withdrawal
        fields = [

       'contact_us','message',
        ]





