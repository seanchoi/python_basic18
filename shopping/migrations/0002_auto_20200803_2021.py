# Generated by Django 3.0.8 on 2020-08-03 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='price',
            new_name='original_price',
        ),
    ]