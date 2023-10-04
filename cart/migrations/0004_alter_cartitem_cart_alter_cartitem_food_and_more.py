# Generated by Django 4.2.5 on 2023-10-02 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
        ('cart', '0003_cartitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart', verbose_name='cart'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food', verbose_name='food'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='quantity'),
        ),
    ]