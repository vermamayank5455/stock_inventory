from django import forms
from django.forms import ModelForm
from store.models import Stock
from store.models import Purchase
from store.models import Sales

class stockform(forms.ModelForm):
    class Meta():
        model = Stock
        fields = '__all__'


class purchaseform(forms.ModelForm):
    class Meta():
        model = Purchase
        fields = '__all__'

class salesform(forms.ModelForm):
    class Meta():
        model = Sales
        fields = '__all__'

