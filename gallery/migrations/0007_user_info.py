# Generated by Django 2.2.9 on 2020-05-22 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20200523_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='info',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
