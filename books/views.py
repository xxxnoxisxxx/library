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
import datetime
from account.models import Reader
from pprint import pprint
from django.utils.timezone import now

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


'''Class represent main view of webpage'''


class DashboardView(LoginRequiredMixin, View):
    template_name = 'index.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name)


'''Class represents view with list all books'''


class BookView(LoginRequiredMixin, View):
    template_name = 'bookWrapper.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        av_books = Item.objects.all().filter(available=True).values_list('books__id', flat=True).distinct()
        return render(request, self.template_name, {'books': books, 'av_books': av_books})


'''Class represent view used for edit books'''


class BookUpdate(LoginAndStaffRequiredMixin, UpdateView):
    model = Book
    template_name = 'book/detail.html'
    fields = ('authors', 'publisher', 'title', 'isbn', 'edition', 'edition_date', 'pages', 'description')

    def get_object(self, *arg, **kwargs):
        return get_object_or_404(Book, id=self.kwargs['id'])


'''Class represents view with list all books'''


class BookListView(LoginAndStaffRequiredMixin, ListView):
    context_object_name = 'books'
    queryset = Book.objects.all()
    template_name = 'book/list.html'

    def dispatch(self, request, *args, **kwargs):
        return super(BookListView, self).dispatch(request, *args, **kwargs)


'''Class represents view to add new books'''


class AddNewBookView(LoginAndStaffRequiredMixin, CreateView):
    model = Book
    template_name = 'add_book.html'
    fields = ('authors', 'publisher', 'title', 'isbn', 'edition', 'edition_date', 'pages', 'description')

    def get_success_url(self):
        return reverse('search_books')
        
        
class AddNewItemView(LoginAndStaffRequiredMixin, CreateView):
    model = Item
    template_name = 'add_item.html'
    fields = ('books', 'available')
    
    def get_success_url(self):
        return reverse('search_books')


'''Class represents view to loan books'''


class LoanView(LoginAndStaffRequiredMixin, View):
    template_name = 'loanWrapper.html'

    def get(self, request, *args, **kwargs):
        items = Item.objects.all().filter(available=True).values_list('books__title', flat=True).distinct()
        books = Book.objects.all().filter(title__in=items)
        readers = Reader.objects.all()
        return render(request, self.template_name, {'books': books, 'readers': readers})


'''Class represents view to return books'''


class ReturnView(LoginAndStaffRequiredMixin, View):
    template_name = 'returnWrapper.html'

    def get(self, request, *args, **kwargs):
        loans = Loan.objects.all().filter(return_date__gt=now())
        todayoffset = now() - datetime.timedelta(days=30)
        return render(request, self.template_name, {'loans': loans, 'todayoffset':todayoffset})


'''Class handle form for loan books'''


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
            loan = Loan(items=item, readers=reader)
            item.save()
            loan.save()
            messages.success(request, 'Enjoy reading')
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(csrf_exempt, name='dispatch')
class  ReservePostView(LoginRequiredMixin, FormView):
    success_url = reverse_lazy('reservebooks')

    def post(self, request, *args, **kwargs):
        reservation = request.body.decode('utf-8')
        data = json.loads(reservation)
        loan = data['selected_books']
        user = data['selected_user']
        print(loan)
        print(user)

        for bookid in reservation:
            item = Item.objects.filter(books__id=bookid, available=True)[:1].get()
            print(item)
            item.available = False
            reader = Reader.objects.get(id=user)
            loan = Loan(items=item, readers=reader)
            item.save()
            loan.save()
            messages.success(request, 'Please come to the Library to receive book.')
        return HttpResponseRedirect(self.get_success_url())
     
        
@method_decorator(csrf_exempt, name='dispatch')
class ReturnPostView(LoginRequiredMixin, FormView):
    success_url = reverse_lazy('search_books')
    
    def post(self, request, *args, **kwargs):
	loan = request.body.decode('utf-8')
	data = json.loads(loan)
	loanid = data['selected_book']
	loan = Loan.objects.get(id=loanid)
	item = Item.objects.get(id=loan.items.id)
	loan.return_date = now()
	loan.save()
	item.available=True
	item.save()
	loan = Loan.objects.get(id=loanid).items.available
	print(loan)
        return HttpResponseRedirect(self.get_success_url())

'''Class represents view with reserved books'''


class ResBookView(LoginRequiredMixin, View):
    template_name = 'reservationWrapper.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        av_books = Item.objects.all().filter(available=True).values_list('books__id', flat=True).distinct()
        return render(request, self.template_name, {'books': books, 'av_books': av_books})


'''Class represents view with list all loaned books'''


class LoanedBookView(LoginRequiredMixin, View):
    template_name = 'loanedBooksWrapper.html'

    def get(self, request, *args, **kwargs):
        loans = Loan.objects.all().filter(readers=request.user.reader)
        print(loans.query)
        return render(request, self.template_name, {'loans': loans})


'''Class represents view with list all books'''


class LoanBookView(LoginRequiredMixin, View):
    template_name = 'bookWrapper.html'

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        return render(request, self.template_name, {'books': books})
