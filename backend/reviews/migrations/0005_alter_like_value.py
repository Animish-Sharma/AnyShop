# Generated by Django 3.2.4 on 2021-07-17 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_like_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.IntegerField(default=1),
        ),
    ]