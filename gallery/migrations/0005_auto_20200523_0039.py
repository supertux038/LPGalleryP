# Generated by Django 2.2.9 on 2020-05-22 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lpmodel',
            options={'ordering': ['-author', '-name', '-difficulty']},
        ),
        migrations.AddField(
            model_name='comment',
            name='on_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.LPModel'),
        ),
        migrations.AddField(
            model_name='lpmodel',
            name='main_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.MainPage'),
        ),
        migrations.AlterField(
            model_name='lpmodel',
            name='difficulty',
            field=models.CharField(choices=[('Л', 'Легкий'), ('С', 'Средний'), ('Т', 'Тяжелый')], max_length=1),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(choices=[('Ю', 'Юзер'), ('М', 'Модератор'), ('А', 'Админ')], max_length=1),
        ),
    ]
