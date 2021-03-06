# Generated by Django 3.2.4 on 2022-03-24 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_refund_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('order_recieved', 'order_recieved'), ('processed', 'processed'), ('shipped', 'shipped'), ('out_for_delivery', 'out_for_delivery'), ('delivered', 'delivered'), ('cancelled', 'cancelled'), ('refund_asked', 'refund_asked'), ('refunded', 'refunded')], max_length=40),
        ),
    ]
