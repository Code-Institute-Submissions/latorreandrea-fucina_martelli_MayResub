# Generated by Django 3.2 on 2022-03-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_orderlineitem_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='lineitem_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
