# Generated by Django 4.0.2 on 2023-02-08 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(upload_to='product/product_cover', verbose_name='Product Image'),
        ),
    ]
