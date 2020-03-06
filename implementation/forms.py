from django import forms
from django.forms import ModelForm
from .models import Nums

class ImplementationForm(forms.ModelForm):
    num1 = forms.FloatField()
    num2 = forms.FloatField()

    class Meta:
        model = Nums
        fields = ('num1', 'num2',)
