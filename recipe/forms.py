from django.forms import ModelForm, forms
from recipe.models import Recipe
from django_summernote.widgets import SummernoteWidget
from django import forms


class RecipeCreateForm(ModelForm):
    class Meta:
        model=Recipe
        fields=[
            'username','recipe_img1','recipe_img2','recipe_img3','recipe_title','recipe_text','recipe_time','food_tag',
        ]
        widgets = {
            'recipe_text': SummernoteWidget(),
            'recipe_time': forms.RadioSelect(),
        }
