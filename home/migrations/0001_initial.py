# Generated by Django 4.1.7 on 2023-03-08 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=40)),
                ('email', models.CharField(default=None, max_length=40, unique=True)),
                ('phone', models.CharField(default=None, max_length=20)),
                ('address', models.CharField(default='', max_length=40)),
                ('password', models.CharField(default=None, max_length=200)),
                ('profile_photo', models.ImageField(blank=True, upload_to='profile/')),
                ('is_seller', models.CharField(default=False, max_length=40)),
                ('seller_slug', models.CharField(default='', max_length=200)),
                ('date_of_register', models.CharField(default=None, max_length=40)),
                ('token', models.CharField(default='', max_length=200)),
                ('status', models.CharField(default='inactive', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(default=None, max_length=30)),
                ('book_slug', models.CharField(default=None, max_length=100)),
                ('book_description', models.CharField(default=None, max_length=50)),
                ('book_category', models.CharField(default=None, max_length=40)),
                ('book_mp', models.CharField(default=None, max_length=10)),
                ('book_discount', models.CharField(default=None, max_length=10)),
                ('book_sp', models.CharField(default=None, max_length=10)),
                ('book_location', models.CharField(default=None, max_length=40)),
                ('book_cover_photo', models.CharField(default=None, max_length=200)),
                ('date_of_added', models.CharField(default='', max_length=40)),
                ('book_status', models.CharField(default='In Stock', max_length=30)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userprofile')),
            ],
        ),
    ]
