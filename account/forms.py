from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from account.models import Reader
from books.models import Book, Author, Publisher


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'isbn', 'edition', 'edition_date', 'pages', 'description')


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'surname')
        labels = {
            'name': _('Author(s) name'),
            'surname': _('Author(s) surname')
        }


class AddPublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name',)
        labels = {
            'name': _('Publisher name')
        }


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
    class Meta:
        model = Reader
        fields = ('id_card', 'mobile')
        labels = {
            'id_card': _('ID card number'),
            'mobile': _('Phone Number')
        }
