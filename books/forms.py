from django import forms
from django.utils.translation import ugettext_lazy as _
from books.models import Book, Author, Publisher


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('authors', 'publisher', 'title', 'isbn', 'edition', 'edition_date', 'pages', 'description')


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
