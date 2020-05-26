from django.contrib.auth.forms import UserCreationForm

from security.models import User


class RegistrationForm(UserCreationForm):

    # CHOICES = (
    #     ('Юзер', 'U')
    #     ('Модератор', '')
    #     ('Админ', 'A')
    # )
    #
    # roles = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
