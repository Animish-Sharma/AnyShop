# Generated by Django 3.2.4 on 2022-05-18 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='banner_img',
            field=models.ImageField(blank=True, null=True, upload_to='banners'),
        ),
    ]
