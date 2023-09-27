# Generated by Django 4.2.5 on 2023-09-27 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_myuser_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Title of User')),
            ],
            options={
                'verbose_name': 'User Type',
            },
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='full_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default=1, max_length=200, verbose_name='First Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default=1, max_length=200, verbose_name='Last Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(db_index=True, max_length=200, verbose_name='Data of Birth'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='type',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.usertype', verbose_name='Type of User'),
        ),
    ]
