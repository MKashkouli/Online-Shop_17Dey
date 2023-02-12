# Generated by Django 4.0.2 on 2023-02-09 13:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_datetime_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=ckeditor.fields.RichTextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]