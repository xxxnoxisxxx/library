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

    def clean_password_confirm(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_confirm']:
            raise forms.ValidationError('Passwords aren\'t match!')
        return cd['password_confirm']


class RegisterReaderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterReaderForm, self).__init__(*args, **kwargs)

        self.fields['mobile'].required = True

    class Meta:
        model = Reader
        fields = ('id_card', 'mobile')
        labels = {
            'id_card': _('ID card number'),
            'mobile': _('Phone Number')
        }
