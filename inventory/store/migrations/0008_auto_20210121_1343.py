# Generated by Django 3.0.1 on 2021-01-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_purchase_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
