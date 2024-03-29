# Generated by Django 2.2.9 on 2020-05-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_auto_20200523_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lpmodel',
            name='image',
            field=models.ImageField(default='user-data/images/renders/default.png', upload_to='user-data/images/renders'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
