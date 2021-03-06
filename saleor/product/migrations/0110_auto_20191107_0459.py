# Generated by Django 2.2.6 on 2019-11-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0109_auto_20191006_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='quantity_allocated',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
