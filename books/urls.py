from django.conf.urls import url
import views

urlpatterns = [
url(r'^$', views.dashboard, name='dashboard'),
url(r'^showbooks/', views.BookView.as_view(), name='bookWrapper'),
]
