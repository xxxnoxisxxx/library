from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import FormView, View
from account.forms import LoginForm, RegisterUserForm, AddBookForm, AddAuthorForm, AddPublisherForm
from account.forms import RegisterReaderForm
from django.contrib import messages
from django.contrib.auth.models import User


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


class AddNewBookView(FormView):
    template_name = 'add_book.html'
    form_class = {'add_book': AddBookForm, 'add_author': AddAuthorForm, 'add_publisher': AddPublisherForm}
    success_url = reverse_lazy('show_books')

    def get(self, request, *args, **kwargs):
        add_book_form = self.form_class['add_book']
        add_author_form = self.form_class['add_author']
        add_publisher_form = self.form_class['add_publisher']
        return render(request, self.template_name,
                      {'add_book': add_book_form, 'add_author': add_author_form, 'add_publisher': add_publisher_form})

    def post(self, request, *args, **kwargs):
        author_form = AddAuthorForm(request.POST)
        publisher_form = AddPublisherForm(request.POST)
        book_form = AddBookForm(request.POST)
        if author_form.is_valid() and publisher_form.is_valid() and book_form.is_valid():
            new_author = author_form.save(commit=False)
            new_author.save()
            new_publisher = publisher_form.save(commit=False)
            new_publisher.save()
            new_book = book_form.save(commit=False)
            new_book.author = new_author
            new_book.publisher = new_publisher
            new_book.save()
            return HttpResponseRedirect(self.get_success_url())
        return render(request, self.template_name,
                      {'add_book': book_form, 'add_author': author_form, 'add_publisher': publisher_form})


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


class LogoutPageView(LoginRequiredMixin, View):
    template_name = 'logout.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            logout(request)
            return render(request, self.template_name)
        else:
            return HttpResponseRedirect(reverse('dashboard'))


def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/list.html', {'section': 'people', 'users': users})


def user_details(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html', {'section': 'people', 'user': user})
