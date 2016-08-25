from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, View
from forms import LoginForm, RegisterUserForm, RegisterReaderForm
from models import Reader
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from forms import LoginForm, RegisterUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class LoginPageView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            print
            request.user
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
    form_class = {'form': RegisterUserForm, 'form_imp': RegisterReaderForm}
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        form = self.form_class['form']
        form_imp = self.form_class['form_imp']
        return render(request, self.template_name, {'form': form, 'form_imp': form_imp})

    def post(self, request, *args, **kwargs):

        #new_form = UserRegistrationForm(request.POST)
        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(self.get_success_url())
        return render(request, self.template_name, {'form': user_form})
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # password_confirm = request.POST.get('password_confirm')
        # email = request.POST.get('email')
        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        # id_card = request.POST.get('id_card')
        # mobile = request.POST.get('mobile')

        #

        # new_user = RegisterUserForm(instance=request.user, data=request.POST)
        # new_reader = RegisterReaderForm(instance=request.reader, data=request.POST)
        # if new_reader.is_valid() and new_user.is_valid():
        #     new_user.save()
        #     new_reader.save()
        # if password == password_confirm:
        #     try:
        #         user = User(username=username, password=password, email=email, first_name=first_name,
        #                     last_name=last_name)
        #         user.save()
        #         reader = Reader(reader=user, id_card=id_card, mobile=mobile)
        #         reader.save()
        #     except IntegrityError:
        #         messages.error(request, u"Input data is not valid!")
        #         form = self.form_class['form']
        #         form_imp = self.form_class['form_imp']
        #         return render(request, self.template_name, {'form': form, 'form_imp': form_imp})
        #     return HttpResponseRedirect(self.get_success_url())
        # else:
        #     messages.error(request, u"Passwords aren't match!")
        # form = self.form_class['form']
        # form_imp = self.form_class['form_imp']
        # return render(request, self.template_name, {'form': form, 'form_imp': form_imp})


class LogoutPageView(LoginRequiredMixin, View):
    template_name = 'logout.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            logout(request)
            return render(request, self.template_name)
        else:
            return HttpResponseRedirect(reverse('dashboard'))
