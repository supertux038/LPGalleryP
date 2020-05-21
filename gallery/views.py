from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.views import View, generic
from django.views.generic import ListView

from gallery.forms import RegistrationForm, LPModelForm
from gallery.models import User

from gallery.models import LPModel


class RegisterView(View):
    def get(self, request):
        return render(request, 'gallery/sign-up.html', {'form': RegistrationForm()})

    def post(self, request):
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(True)
            form.save_m2m()
            return redirect(reverse('login'))

        return render(request, 'gallery/registration.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'gallery/login.html', {'form': AuthenticationForm})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is None:
                return render(
                    request,
                    'gallery/login.html',
                    {'form': form, 'invalid_creds': True}
                )

            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'gallery/login.html',
                    {'form': form, 'invalid_creds': True}
                )
            login(request, user)

            return redirect(reverse('main'))


def logout_func(request):
    logout(request)
    return redirect('main')


@login_required
def user_page(request, username):
    try:
        user = User.objects.get(username=username)
        models = LPModel.objects.filter(author=user)
        return render(request, 'gallery/user-page.html', {'author': user})
    except ObjectDoesNotExist:
        return render(request, 'gallery/user-not-exists.html')


def main(request):
    print(settings.USER_AVATAR_DIRECTORY)
    return render(request, 'gallery/main.html', {})


def model(request, num):
    print(num)
    lp_model = LPModel(name='AE86', description='Описание из вьюхи', difficulty='Легкое',
                       category='Транспорт')
    return render(request, 'gallery/model-page.html', {'model': lp_model})


def communities(request):
    return render(request, '500.html')


class AuthorList(ListView):
    model = User
    template_name = 'gallery/authors.html'
    context_object_name = 'authors'


class AddModelView(LoginRequiredMixin, generic.FormView):
    form_class = LPModelForm
    template_name = 'gallery/add-model.html'
    # success_url = reverse_lazy('user-page', self.request.user.username)


def page_not_found(request, exception):
    # print(exception)
    return render(request, '404.html')


def internal_server_error(request):
    return render(request, '500.html')
