# Generated by Django 2.2.9 on 2020-05-22 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20200523_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lpmodel',
            name='image_path',
        ),
        migrations.AddField(
            model_name='lpmodel',
            name='image',
            field=models.ImageField(default='user-data/images/avatars/default.png', upload_to='user-data/models/../renders'),
        ),
    ]