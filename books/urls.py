import views
from django.conf.urls import url

from books.views import *

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^searchbooks/', BookView.as_view(), name='search_books'),
    url(r'^reservebooks/', ResBookView.as_view(), name='reserve_books'),
    url(r'^loan_book/', LoanView.as_view(), name='loan_book'),
    url(r'^return_book/', ReturnView.as_view(), name='return_book'),
    url(r'^loaned_books/', LoanedBookView.as_view(), name='loaned_books'),
    url(r'^add_book', AddNewBookView.as_view(), name='add_book'),
    url(r'^edit_book/$', BookListView.as_view(), name='edit_book_list'),
    url(r'^edit_book/(?P<id>\d+)/$', BookUpdate.as_view(), name='book_update'),
    url(r'^loan/', LoanPostView.as_view(), name='loan'),

]

