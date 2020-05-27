from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from rest_framework import viewsets, permissions

from security.forms import RegistrationForm
from security.models import User
from security.serializers import UserSerializer


class RegisterView(View):
    def get(self, request):
        return render(request, 'security/registration.html', {'form': RegistrationForm})

    def post(self, request):
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(True)
            form.save_m2m()
            return redirect(reverse('security:login'))

        return render(request, 'security/registration.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'security/login.html', {'form': AuthenticationForm})

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
                    'security/login.html',
                    {'form': form, 'invalid_creds': True}
                )

            try:
                form.confirm_login_allowed(user)
            except ValidationError:
                return render(
                    request,
                    'security/login.html',
                    {'form': form, 'invalid_creds': True}
                )
            login(request, user)

            return redirect(reverse('gallery:main'))
        else:
            return render(request, 'security/login.html', {'form': form})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-username')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


def logout_func(request):
    logout(request)
    return redirect('gallery:main')


def page_not_found(request, exception):
    return render(request, '404.html')


def internal_server_error(request):
    return render(request, '500.html')