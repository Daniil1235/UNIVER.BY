from django.forms import ModelForm, Textarea, TextInput, DateTimeInput, Select, RadioSelect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "photo", "user_type")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user