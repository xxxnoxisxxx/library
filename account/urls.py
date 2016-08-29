from django.conf.urls import url

from account.views import LoginPageView, LogoutPageView, RegisterNewUserView, user_details, user_list

urlpatterns = [
    url(r'^login/', LoginPageView.as_view(), name='login'),
    url(r'^logout/', LogoutPageView.as_view(), name='logout'),
    url(r'^register/', RegisterNewUserView.as_view(), name='register'),
    url(r'^user/$', user_list, name='user_list'),
    url(r'^user/(?P<username>[-\w]+)/$', user_details, name='user_detail'),
]
