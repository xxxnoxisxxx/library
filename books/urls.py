from django.conf.urls import url
import views
from books.views import AddNewBookView, BookListView, BookUpdate

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^showbooks/', views.BookView.as_view(), name='show_books'),
    url(r'^loan_book/', views.LoanView.as_view(), name='loan_book'),
    url(r'^add_book', AddNewBookView.as_view(), name='add_book'),
    url(r'^edit_book/', BookListView.as_view(), name='edit_book_list'),
    url(r'^edit_book/(?P<id>\d+)/$', BookUpdate.as_view(), name='book_update'),
]

