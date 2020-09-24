# Generated by Django 3.0.8 on 2020-08-03 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_auto_20200803_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='product_id',
        ),
        migrations.AddField(
            model_name='price',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='price', to='shopping.Product'),
        ),
    ]
