# Generated by Django 4.2.5 on 2023-10-04 07:01

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import user.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='address')),
                ('location', django.contrib.gis.db.models.fields.GeometryField(blank=True, geography=True, null=True, srid=4326, verbose_name='location')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(db_index=True, max_length=11, unique=True, validators=[user.validators.check_phone], verbose_name='Mobile Phone Number')),
            ],
            options={
                'verbose_name': 'User',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'User Type',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.myuser', verbose_name='User Id')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('birth_date', models.DateField(db_index=True, max_length=200, verbose_name='Data of Birth')),
                ('slug', models.SlugField(blank=True, max_length=200, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'User Profile',
            },
        ),
        migrations.AddField(
            model_name='myuser',
            name='type',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.usertype', verbose_name='Type of User'),
        ),
    ]
