# Generated by Django 3.2 on 2022-03-01 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(max_length=100),
        ),
    ]
