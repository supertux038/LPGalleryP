from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.validators import FileExtensionValidator
from django.views.generic import UpdateView

from gallery.models import LPModel
from security.models import User


class LPModelForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea, label='Большое описание (используется на странице модели)')
    file = forms.FileField(required=True, validators=[FileExtensionValidator(allowed_extensions=['babylon'],
                                                                             message='Неверный формат файла')],
                           label='Файл модели в формате .babylon')
    image = forms.ImageField(required=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'],
                                                                               message='Неверный формат файла')])

    class Meta:
        model = LPModel
        fields = ('name', 'description', 'small_description', 'file', 'video_lesson_link',
                  'image', 'difficulty', 'category')
        labels = {
            'name': 'Название',
            'small_description': 'Мальнькое описание (используется в карточке модели)',
            'video_lesson_link': 'Ссылка на видео на YouTube по созданию модели',
            'image': 'Изображение, которое будет использоваться как аватар модели',
            'difficulty': 'Сложность',
            'category': 'Категория',
        }


class UpdateUserForm(forms.Form):
    info = forms.TextInput()
    avatar_photo = forms.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'],
                                                                       message='Неверный формат файла')],
                                    required=False)

    class Meta:
        model = User
        fields = (
            'avatar_photo',
            'info')
        labels = {
            'avatar_photo': 'Картинка для аватарке в формате .jpg или .png'
        }


class CommentForm(forms.Form):
    text = forms.Textarea()
    model_id = forms.HiddenInput()
