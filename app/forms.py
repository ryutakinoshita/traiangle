from django.forms import ModelForm
from app.models import Withdrawal




class ContactForm(ModelForm):
    class Meta:
        model = Withdrawal
        fields = [
            'contact_us','message',
        ]







