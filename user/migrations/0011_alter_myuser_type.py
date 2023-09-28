# Generated by Django 4.2.5 on 2023-09-27 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_myuser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='type',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.usertype', verbose_name='Type of User'),
        ),
    ]
