# Generated by Django 3.0.8 on 2020-08-03 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20200803_2021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='produc_id',
            new_name='product_id',
        ),
    ]
