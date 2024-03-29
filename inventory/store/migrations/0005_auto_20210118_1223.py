# Generated by Django 3.0.1 on 2021-01-18 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210116_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Stock'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
