from django.conf.urls import url

from account.views import LoginPageView, LogoutPageView, RegisterNewUserView

urlpatterns = [
    url(r'^login/', LoginPageView.as_view(), name='login'),
    url(r'^logout/', LogoutPageView.as_view(), name='logout'),
    url(r'^register/$', RegisterNewUserView.as_view(), name='register'),

]
