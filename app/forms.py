from django.forms import ModelForm
from app.models import Withdrawal, Contact


class ContactForm(ModelForm):
    class Meta:
        model = Withdrawal
        fields = [
            'contact_us','message',
        ]



class ContactRestForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            'contact_us','message',
        ]







