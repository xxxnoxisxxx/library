import json

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView, View, ListView, DetailView, UpdateView, CreateView
from django.views.decorators.csrf import csrf_exempt
from books.forms import AddBookForm, AddAuthorForm, AddPublisherForm
from books.models import Book, Item, Loan
from account.models import Reader
from pprint import pprint

# LOGIN ACCESS REQUIRED
class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

# LOGIN ACCESS REQUIRED
# ONLY FOR STAFF
class LoginAndStaffRequiredMixin(object):
    @method_decorator(login_required)
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginAndStaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class DashboardView(LoginRequiredMixin, View):
    template_name = 'index.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name)


class BookView(LoginRequiredMixin, View):
    template_name = 'bookWrapper.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        return render(request, self.template_name, {'books': books})


class BookUpdate(LoginAndStaffRequiredMixin,UpdateView):

    model = Book
    template_name = 'book/detail.html'
    fields = ('authors','publisher','title', 'isbn', 'edition', 'edition_date', 'pages', 'description')

    def get_object(self, *arg, **kwargs):
        return get_object_or_404(Book, id=self.kwargs['id'])


class BookListView(LoginAndStaffRequiredMixin, ListView):
    context_object_name = 'books'
    queryset = Book.objects.all()
    template_name = 'book/list.html'

    def dispatch(self, request, *args, **kwargs):
        return super(BookListView, self).dispatch(request, *args, **kwargs)


class AddNewBookView(LoginAndStaffRequiredMixin, CreateView):
    model = Book
    template_name = 'add_book.html'
    fields = ('authors','publisher','title', 'isbn', 'edition', 'edition_date', 'pages', 'description')

    def get_success_url(self):
        return reverse('search_book')

class LoanView(LoginAndStaffRequiredMixin, View):
    template_name = 'loanWrapper.html'

    def get(self, request, *args, **kwargs):
        items = Item.objects.all().filter(available=True).values_list('books__title', flat=True).distinct()
        books = Book.objects.all().filter(title__in=items)
        readers = Reader.objects.all()
        return render(request, self.template_name, {'books': books, 'readers': readers})

class ReturnView(LoginAndStaffRequiredMixin, View):
    template_name = 'returnWrapper.html'

    def get(self, request, *args, **kwargs):
        items = Item.objects.all().filter(available=True).values_list('books__title', flat=True).distinct()
        books = Book.objects.all().filter(title__in=items)
        return render(request, self.template_name, {'books': books})


@method_decorator(csrf_exempt, name='dispatch')
class LoanPostView(LoginRequiredMixin, FormView):
    success_url = reverse_lazy('loan_book')
   

    def post(self, request, *args, **kwargs):
        loan = request.body.decode('utf-8')
        data = json.loads(loan)
        loan = data['selected_books']
        user = data['selected_user']
        print(loan)
        print(user)
        for bookid in loan:
            item = Item.objects.filter(books__id=bookid, available=True)[:1].get()
            print(item)
            item.available = False
            reader = Reader.objects.get(id=user)
            loan = Loan(items = item, readers = reader)
            item.save()
            loan.save()
            messages.success(request, 'Enjoy reading')
        return HttpResponseRedirect(self.get_success_url())


class ResBookView(LoginRequiredMixin, View):
    template_name = 'bookWrapper.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        return render(request, self.template_name, {'books': books})


class LoanedBookView(LoginRequiredMixin, View):
    template_name = 'loanedBooksWrapper.html'

    def get(self, request, *args, **kwargs):
        items = Item.objects.all().filter(available=True).values_list('books__title', flat=True).distinct()
        books = Book.objects.all().filter(title__in=items)
        return render(request, self.template_name, {'books': books})


class LoanBookView(LoginRequiredMixin, View):
    template_name = 'bookWrapper.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        return render(request, self.template_name, {'books': books})
