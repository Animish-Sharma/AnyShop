# Generated by Django 3.2.4 on 2022-05-06 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_auto_20220424_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='address',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
