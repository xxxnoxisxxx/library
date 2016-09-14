from django import forms
from django.utils.translation import ugettext_lazy as _
from books.models import Book, Author, Publisher
from django.contrib.admin import widgets


class AddBookForm(forms.ModelForm):
    """Class represents form for adding new books to library"""
    class Meta:
        model = Book
        fields = ('authors', 'publisher', 'title', 'isbn', 'edition', 'edition_date', 'pages', 'description')
        widgets = {
            'edition_date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(AddBookForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True


class AddAuthorForm(forms.ModelForm):
    """Class represents form for adding new authors of books to library"""
    class Meta:
        model = Author
        fields = ('name', 'surname')
        labels = {
            'name': _('Author(s) name'),
            'surname': _('Author(s) surname')
        }


class AddPublisherForm(forms.ModelForm):
    """Class represents form for adding new publishers of books to library"""
    class Meta:
        model = Publisher
        fields = ('name',)
        labels = {
            'name': _('Publisher name')
        }
