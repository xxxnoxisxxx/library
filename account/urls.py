from django.conf.urls import url
from account.views import LoginPageView, LogoutPageView

urlpatterns = [
	url(r'^login/', LoginPageView.as_view(), name='login'),
	url(r'^logout/', LogoutPageView.as_view(), name='logout'),
]
