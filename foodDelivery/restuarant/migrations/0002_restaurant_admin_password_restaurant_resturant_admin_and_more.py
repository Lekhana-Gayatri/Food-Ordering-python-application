# Generated by Django 4.2.13 on 2024-05-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restuarant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='admin_password',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='resturant_admin',
            field=models.EmailField(default='me', max_length=254),
        ),
        migrations.AlterField(
            model_name='dish',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3, null=True),
        ),
    ]
