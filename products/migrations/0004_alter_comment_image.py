# Generated by Django 4.0.2 on 2023-02-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_comment_image_alter_comment_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(upload_to='covers/', verbose_name='Product Image'),
        ),
    ]