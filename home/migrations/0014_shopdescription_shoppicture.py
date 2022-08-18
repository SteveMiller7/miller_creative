# Generated by Django 3.2 on 2022-08-18 16:05

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_featuredcompany_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='ShopDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.shoppicture')),
            ],
            options={
                'verbose_name_plural': 'Shop Description',
            },
        ),
    ]
