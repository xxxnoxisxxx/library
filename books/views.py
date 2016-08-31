from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView, View
from books.models import Book, Item

from books.forms import AddBookForm, AddAuthorForm, AddPublisherForm


# Create your views here.

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class DashboardView(LoginRequiredMixin, View):
    template_name = 'index.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name)


class BookView(LoginRequiredMixin, View):
    template_name = 'bookWrapper.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        return render(request, self.template_name, {'books': books})


class AddNewBookView(FormView):
    template_name = 'add_book.html'
    form_class = {'add_book': AddBookForm, 'add_author': AddAuthorForm, 'add_publisher': AddPublisherForm}
    success_url = reverse_lazy('show_books')

    def get(self, request, *args, **kwargs):
        add_book_form = self.form_class['add_book']
        add_author_form = self.form_class['add_author']
        add_publisher_form = self.form_class['add_publisher']
        return render(request, self.template_name,
                      {'add_book': add_book_form, 'add_author': add_author_form, 'add_publisher': add_publisher_form})

    def post(self, request, *args, **kwargs):
        author_form = AddAuthorForm(request.POST)
        publisher_form = AddPublisherForm(request.POST)
        book_form = AddBookForm(request.POST)
        if author_form.is_valid() and publisher_form.is_valid() and book_form.is_valid():
            new_author = author_form.save(commit=False)
            new_author.save()
            new_publisher = publisher_form.save(commit=False)
            new_publisher.save()
            new_book = book_form.save(commit=False)
            new_book.author = new_author
            new_book.publisher = new_publisher
            new_book.save()
            return HttpResponseRedirect(self.get_success_url())
        return render(request, self.template_name,
                      {'add_book': book_form, 'add_author': author_form, 'add_publisher': publisher_form})


class LoanView(LoginRequiredMixin, View):
    template_name = 'loanWrapper.html'

    def get(self, request, *args, **kwargs):
        items = Item.objects.all().filter(available=True).values_list('books__title', flat=True).distinct()
        books = Book.objects.all().filter(title__in=items)
        return render(request, self.template_name, {'books': books})


def Loan(request):
    if request.is_ajax():
        print
        "ASDADADADASD"
        request_data = request.POST
        return HttpResponse("OK")
