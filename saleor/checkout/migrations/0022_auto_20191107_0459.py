# Generated by Django 2.2.6 on 2019-11-07 10:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0021_django_price_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='checkoutline',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]