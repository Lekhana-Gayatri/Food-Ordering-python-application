# Generated by Django 4.2.13 on 2024-07-13 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restuarant', '0009_resadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='password',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='resturant_admin',
        ),
    ]
