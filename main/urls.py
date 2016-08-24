from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^a/', views.opcja1, name='opcja1'),
]
