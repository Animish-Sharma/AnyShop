# Generated by Django 3.2.4 on 2021-07-14 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_1',
            field=models.ImageField(blank=True, help_text='if any', null=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, help_text='if any', null=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, help_text='if any', null=True, upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_4',
            field=models.ImageField(blank=True, help_text='if any', null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('tech', 'Technology'), ('books', 'Books'), ('apparel', 'Apparel'), ('h&k', 'Home Kitchen'), ('beauty', 'Beauty'), ('t&g', 'Toys Games'), ('home', 'Home Entertainment'), ('luggage', 'Luggage')], max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products'),
        ),
    ]
