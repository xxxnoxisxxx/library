from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from models import Book
# Create your views here.

# from django.contrib.admin.views.decorators import staff_member_required

# @staff_member_required

@login_required
def dashboard(request):
	return render(request,'index.html', {})
	
class BookView(View):
	template_name = 'bookWrapper.html'

	def get(self, request, *args, **kwargs):
		books = Book.objects.all()
		return render(request, self.template_name, {'books':books})
