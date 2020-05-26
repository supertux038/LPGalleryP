from django import forms
from django.contrib.auth.forms import UserCreationForm

from gallery.models import User, LPModel


class LPModelForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = LPModel
        fields = ('name', 'description', 'small_description', 'file', 'video_lesson_link',
                  'image', 'difficulty', 'category')
        labels = {
            'name': 'Название',
            'description': 'Большое описание (используется на странице модели)',
            'small_description': 'Мальнькое описание (используется в карточке модели)',
            'file': 'Файл модели в формате .babylon',
            'video_lesson_link': 'Ссылка на видео на YouTube по созданию модели',
            'image': 'Изображение, которое будет использоваться как аватар модели',
            'difficulty': 'Сложность',
            'category': 'Категория',
        }
