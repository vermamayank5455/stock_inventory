# Generated by Django 3.0.1 on 2021-01-16 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210113_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Stock'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
