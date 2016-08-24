from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, View

from forms import LoginForm, RegisterUserForm


# Create your views here.

# class LoginRequiredMixin(object):
# 	@method_decorator(login_required)
# 	def dispatch(self, request, *args, **kwargs):
# 		return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class LoginPageView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            print request.user
            return HttpResponseRedirect(self.get_success_url())
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(self.get_success_url())
        form = self.form_class
        return render(request, self.template_name, {'form': form})


class RegisterNewUserView(FormView):
    template_name = 'register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        #
        # print(username)
        # print (password)
        # print (password_confirm)
        # print (email)
        # print (first_name)
        # print (last_name)
        #
        if password == password_confirm:
            print ("Passwords match!")
            user = User(username=username, password=password, email=email, first_name=first_name,
                        last_name=last_name)
            user.save()
        form = self.form_class
        return render(request, self.template_name, {'form': form})


class LogoutPageView(View):
    template_name = 'logout.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            logout(request)
            return render(request, self.template_name)
        else:
            return HttpResponseRedirect(reverse('dashboard'))
