# Generated by Django 4.0.2 on 2023-02-19 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_alter_order_order_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='authority',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=700, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_notes',
            field=models.CharField(blank=True, max_length=700, verbose_name='Order Note'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
