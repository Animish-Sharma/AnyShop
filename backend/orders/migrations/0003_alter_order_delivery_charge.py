# Generated by Django 3.2.4 on 2022-03-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_delivery_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_charge',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
