from django import forms
from django.forms import ModelForm

from app.models import Withdrawal, Contact,GameForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = [
            'contact_us','message',
        ]



class ContactRestForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'contact_us','message',
        ]

class PostGameForm(ModelForm):
    class Meta:
        model = GameForm
        fields = (
            'games',
        )







