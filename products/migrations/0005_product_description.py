# Generated by Django 4.1.3 on 2022-11-23 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_category_product_categorykey'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=3, max_length=500),
            preserve_default=False,
        ),
    ]
