# Generated by Django 2.2.9 on 2020-05-26 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0014_auto_20200526_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
