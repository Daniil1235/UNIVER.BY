from premium.models import License
from django import forms
from django.forms import ModelForm, TextInput


class LicenseForm(ModelForm):
    class Meta:
        model = License
        fields = ['key']
        widgets = {
            'key': TextInput(attrs={'class': 'form-control',
                                    'placeholder': 'Ключ лицензии'}),
        }
