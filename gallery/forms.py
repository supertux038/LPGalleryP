from django import forms
from django.contrib.auth.forms import UserCreationForm

from gallery.models import User, LPModel


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'roles')


class LPModelForm(forms.ModelForm):
    class Meta:
        model = LPModel
        fields = '__all__'
