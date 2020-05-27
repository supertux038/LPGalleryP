from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.generic import ListView, UpdateView
from rest_framework import viewsets, permissions

from LPGallery import env_settings as _env
from gallery.forms import LPModelForm, UpdateUserForm, CommentForm
from gallery.models import LPModel, Comment, Community, MainPage
from security.models import User
from gallery.serializers import CommunitySerializer, LPModelSerializer, CommentSerializer, MainPageSerializer


@login_required
def user_page(request, username=None):
    if username is not None:
        print(username)
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return render(request, 'gallery/user-not-exists.html')
    else:
        user = request.user
    lp_models = LPModel.objects.filter(author=user)
    return render(request, 'gallery/user-page.html', {'author': user, 'models': lp_models})


def main(request):
    main_page = MainPage.objects.get(name=_env.MAIN_PAGE)
    lp_models = LPModel.objects.filter(main_page=main_page.id)
    return render(request, 'gallery/main.html', {'main_page': main_page, 'models': lp_models})


def model(request, num):
    lp_model = LPModel.objects.get(id=num)
    comments = Comment.objects.filter(on_model=lp_model).order_by('-creation_time')
    return render(request, 'gallery/model-page.html', {'model': lp_model, 'comments': comments})


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


class UserUpdate(UpdateView):
    model = User
    fields = ['info', 'avatar_photo']
    template_name_suffix = '_update_form'


class AddModelView(LoginRequiredMixin, generic.FormView):
    form_class = LPModelForm
    template_name = 'gallery/add-model-test.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        lp_model = form.save()
        return redirect('gallery:user_page', user)


@login_required
def add_comment(request):
    if request.method == 'POST':
        text = request.POST['text']
        model_id = request.POST['on_model']
        print(model_id)
        on_model = LPModel.objects.get(id=model_id)
        if len(text) < 280:
            comment = Comment.objects.create(on_model=on_model, text=text, author=request.user, creation_time=timezone.now())
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def page_not_found_test(request):
    return render(request, '404.html')


def internal_server_error_test(request):
    return render(request, '500.html')


def edit_profile(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('gallery:user_page', request.user)

    else:
        form = UpdateUserForm(request.user)
        return render(request, 'gallery/edit-user.html', {'form': form})


class ModelDelete(generic.DeleteView):
    model = LPModel
    success_url = reverse_lazy('gallery:user_page')
    template_name = 'gallery/model-delete.html'


# def remove_model(request, model_id):
#     lp_model = LPModel.objects.get(id=model_id)
#     if lp_model.author == request.user:
#         lp_model.delete()
#     return redirect('gallery:user_page', request.user)


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticated]


class LPModelViewSet(viewsets.ModelViewSet):
    queryset = LPModel.objects.all()
    serializer_class = LPModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('creation_time')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class MainPageViewSet(viewsets.ModelViewSet):
    queryset = MainPage.objects.all().order_by('name')
    serializer_class = MainPageSerializer
    permission_classes = [permissions.IsAdminUser]
