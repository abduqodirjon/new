# Generated by Django 3.1.13 on 2021-12-08 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_customimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='image',
        ),
    ]
