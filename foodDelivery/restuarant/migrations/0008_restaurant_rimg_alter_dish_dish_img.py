# Generated by Django 4.2.13 on 2024-05-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restuarant', '0007_dish_dish_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='rimg',
            field=models.ImageField(blank=True, null=True, upload_to='dishes/'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='dish_img',
            field=models.ImageField(blank=True, null=True, upload_to='dishes/'),
        ),
    ]
