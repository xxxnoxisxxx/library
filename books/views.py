from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from models import Book, Item
from django.utils.decorators import method_decorator
# Create your views here.

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class DashboardView(LoginRequiredMixin, View):
	template_name = 'index.html'

	def get(self, request, *arg, **kwargs):
		return render (request, self.template_name)

class BookView(LoginRequiredMixin, View):
	template_name = 'bookWrapper.html'

	def get(self, request, *args, **kwargs):
		books = Book.objects.all()
		return render(request, self.template_name, {'books':books})
		
		
class LoanView(LoginRequiredMixin, View):
	template_name = 'loanWrapper.html'

	def get(self, request, *args, **kwargs):
		items = Item.objects.all().filter(available = True).values_list('books__title',flat=True).distinct()
		books = Book.objects.all().filter(title__in=items)
		return render(request, self.template_name, {'books':books})
		

def Loan(request):
	if request.POST:
		if request.is_ajax():
			print "ASDADADADASD"
			request_data = request.POST
			return HttpResponse("OK")

			

