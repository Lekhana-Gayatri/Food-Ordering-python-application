# Generated by Django 4.2.13 on 2024-05-24 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restuarant', '0006_alter_restaurant_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='dish_img',
            field=models.ImageField(default=2, upload_to='dishes'),
            preserve_default=False,
        ),
    ]
