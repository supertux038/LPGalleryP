from django.contrib.auth.forms import UserCreationForm

from security.models import User


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
