import views
from django.conf.urls import url

from books.views import BookListView, BookUpdate
from books.views import DashboardView, AddNewBookView, LoanView, BookView

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^showbooks/', BookView.as_view(), name='show_books'),
    url(r'^loan_book/', LoanView.as_view(), name='loan_book'),
    url(r'^add_book', AddNewBookView.as_view(), name='add_book'),
    url(r'^edit_book/$', BookListView.as_view(), name='edit_book_list'),
    url(r'^edit_book/(?P<id>\d+)/$', BookUpdate.as_view(), name='book_update'),
    url(r'^loan/', views.Loan.as_view(), name='loan'),

]

