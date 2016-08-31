from django.conf.urls import url
from account.views import LoginPageView, LogoutPageView, RegisterNewUserView, UserListPageView, UserDetailsPageView, AddNewBookView
urlpatterns = [
    url(r'^login/', LoginPageView.as_view(), name='login'),
    url(r'^logout/', LogoutPageView.as_view(), name='logout'),
    url(r'^register/', RegisterNewUserView.as_view(), name='register'),
    url(r'^user/$', UserListPageView.as_view(), name='user_list'),
    url(r'^user/(?P<username>[-\w]+)/$', UserDetailsPageView.as_view(), name='user_detail'),
    url(r'^add_book', AddNewBookView.as_view(), name='add_book'),
]
