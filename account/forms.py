from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from models import Reader


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True

    def clean_username(self):
        data = self.cleaned_data['username']
        raise forms.ValidationError("WAWWWWWWWWWWWWWWWWWWWWWWWWWW")
        return data

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


class RegisterReaderForm(forms.ModelForm):

    class Meta:
        model = Reader
        fields = ('id_card', 'mobile')
        labels = {
            'id_card': _('ID card number'),
            'mobile': _('Phone Number')
        }
