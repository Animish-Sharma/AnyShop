# Generated by Django 3.2.4 on 2022-03-31 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='appartment_address',
            new_name='apartment_address',
        ),
    ]
