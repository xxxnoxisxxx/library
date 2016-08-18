from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import FormView, View
from forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
# Create your views here.

class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class LoginPageView(FormView):
	template_name = 'login.html'
	form_class = LoginForm
	success_url = '/'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			print request.user
			return HttpResponseRedirect(self.get_success_url())
		form = self.form_class
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(self.get_success_url())
		form = self.form_class
		return render(request, self.template_name, {'form':form})

class LogoutPageView(View):
	template_name = 'logout.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			logout(request)
			return render(request, self.template_name)
		else:
			return HttpResponseRedirect('/')
