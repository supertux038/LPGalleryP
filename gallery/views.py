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

from LPGallery import env_settings as _env

from gallery.forms import LPModelForm
from gallery.models import User, MainPage

from gallery.models import LPModel


@login_required
def user_page(request, username):
    try:
        user = User.objects.get(username=username)
        lp_models = LPModel.objects.filter(author=user)
        return render(request, 'gallery/user-page.html', {'author': user, 'models': lp_models})
    except ObjectDoesNotExist:
        return render(request, 'gallery/user-not-exists.html')


def main(request):
    main_page = MainPage.objects.get(name=_env.MAIN_PAGE)
    lp_models = LPModel.objects.filter(main_page=main_page.id)
    return render(request, 'gallery/main.html', {'main_page': main_page, 'models': lp_models})


def model(request, num):
    lp_model = LPModel.objects.get(id=num)
    return render(request, 'gallery/model-page.html', {'model': lp_model})


def communities(request):
    return render(request, '500.html')


def models(request, param=None, argument=None):
    if param is not None:
        if param == 'category':
            lp_models = LPModel.objects.filter(category=argument)
        elif param == 'difficulty':
            lp_models = LPModel.objects.filter(difficulty=argument)
        else:
            lp_models = None
    else:
        lp_models = LPModel.objects.all()
    return render(request, 'gallery/models.html', {'models': lp_models})


class AuthorList(ListView):
    model = User
    template_name = 'gallery/authors.html'
    context_object_name = 'authors'


class AddModelView(LoginRequiredMixin, generic.FormView):
    form_class = LPModelForm
    template_name = 'gallery/add-model-test.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        lp_model = form.save()
        return redirect('gallery:user_page', user)


# def add_comment(request):
#     if


def page_not_found_test(request):
    return render(request, '404.html')


def internal_server_error_test(request):
    return render(request, '500.html')
