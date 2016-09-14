from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator

from django.views.generic import FormView, View, ListView, DetailView
from account.forms import LoginForm, RegisterUserForm
from account.forms import RegisterReaderForm
from django.views.generic import FormView, View, ListView, DetailView
from account.forms import LoginForm, RegisterUserForm
from account.forms import RegisterReaderForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

'''
Use this class for login required
'''


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


'''
This class represent view with form to login into library
on GET request we have form to input our credentials
on POST request we check given input and if they are valid login into.
'''


class LoginPageView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user_form = LoginForm(request.POST)
        if user_form.is_valid():
            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(self.get_success_url())
            else:
                messages.error(request, 'User not found. Please enter correct parameters.')
        return render(request, self.template_name, {'form': user_form})


'''
This class represent view with form to register new user
on GET request we have form to input data about new user
on POST request we check given input and if they are new user is added into database
'''


class RegisterNewUserView(FormView):
    template_name = 'register_user.html'
    form_class = {'form': RegisterUserForm, 'form_imp': RegisterReaderForm}
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        form = self.form_class['form']
        form_imp = self.form_class['form_imp']
        return render(request, self.template_name, {'form': form, 'form_imp': form_imp})

    def post(self, request, *args, **kwargs):
        user_form = RegisterUserForm(request.POST)
        form_imp = RegisterReaderForm(request.POST)
        if user_form.is_valid() and form_imp.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            reader = form_imp.save(commit=False)
            reader.reader = new_user
            reader.save()
            return HttpResponseRedirect(self.get_success_url())
        return render(request, self.template_name, {'form': user_form, 'form_imp': form_imp})


'''
This class represent view with logout response
'''


class LogoutPageView(LoginRequiredMixin, View):
    template_name = 'logout.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            logout(request)
            return render(request, self.template_name)
        else:
            return HttpResponseRedirect(reverse('dashboard'))


'''
This class represent view list all active users
'''


class UserListPageView(LoginRequiredMixin, ListView):
    context_object_name = 'users'
    queryset = User.objects.filter(is_active=True).exclude(username='admin')
    template_name = 'account/user/list.html'

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserListPageView, self).dispatch(request, *args, **kwargs)


'''
This class represent detail view for selected user
'''


class UserDetailsPageView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'account/user/detail.html'
    context_object_name = 'user'

    def get_object(self, *arg, **kwargs):
        return get_object_or_404(User, username=self.kwargs['username'])

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserDetailsPageView, self).dispatch(request, *args, **kwargs)
