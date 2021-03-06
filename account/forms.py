from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from account.models import Reader


class LoginForm(forms.Form):
    """Class represent form for login into library
        Fields username and password are required
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterUserForm(forms.ModelForm):
    """Class represent form for adding new library user
        This class also check that password and confirm password match to each other
    """
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
    """Class represent form for additional data used in registration form"""
    class Meta:
        model = Reader
        fields = ('id_card', 'mobile')
        labels = {
            'id_card': _('ID card number'),
            'mobile': _('Phone Number')
        }
