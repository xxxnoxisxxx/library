from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password_confirm')
        widgets = {
            'password': forms.PasswordInput(),
            'password_confirm': forms.PasswordInput(),
        }
        labels = {
            'password': _('Password'),
            'password_confirm': _('Confirm password')
        }