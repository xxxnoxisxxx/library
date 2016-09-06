import json

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView, View
from django.views.generic import ListView, DetailView

from books.forms import AddBookForm, AddAuthorForm, AddPublisherForm
from books.models import Book, Item


# Create your views here.

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class LoginAndStaffRequiredMixin(object):
    @method_decorator(login_required)
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginAndStaffRequiredMixin, self).dispatch(request, *args, **kwargs)


# ONLY FOR STAFF
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class DashboardView(LoginRequiredMixin, View):
    template_name = 'index.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name)


class BookView(LoginRequiredMixin, View):
    template_name = 'bookWrapper.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        return render(request, self.template_name, {'books': books})


class BookUpdate(DetailView):
    model = Book
    template_name = 'book/detail.html'
    context_object_name = 'BOOK'

    def get_object(self, *arg, **kwargs):
        return get_object_or_404(Book, id=self.kwargs['id'])

    def dispatch(self, request, *args, **kwargs):
        return super(BookUpdate, self).dispatch(request, *args, **kwargs)


class BookListView(ListView):
    context_object_name = 'books'
    queryset = Book.objects.all()
    template_name = 'book/list.html'

    def dispatch(self, request, *args, **kwargs):
        return super(BookListView, self).dispatch(request, *args, **kwargs)



        # ONLY FOR STAFF


class AddNewBookView(LoginAndStaffRequiredMixin, FormView):
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

    from django.views.decorators.csrf import csrf_exempt

    @method_decorator(csrf_exempt, name='dispatch')


class Loan(LoginRequiredMixin, View):
    success_url = reverse_lazy('loan_book')

    def post(self, request, *args, **kwargs):
        loan = request.body.decode('utf-8')
        loan = json.loads(loan)['selected']
        for bookid in loan:
            item = Item.objects.filter(books__id=bookid, available=True)[:1].get()
            print(item.available)
            item.available = False
            item.save()
            print(item)
            messages.success(request, 'Enjoy reading')
        return HttpResponseRedirect(self.get_success_url())