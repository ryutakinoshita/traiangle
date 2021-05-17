from django import forms
from .models import Individual


class IndividualForm(forms.ModelForm):

    class Meta:
        model = Individual
        fields = ("zip_code", "prefectures", "city", "address1","address2")