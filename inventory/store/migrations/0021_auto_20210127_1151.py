# Generated by Django 3.0.1 on 2021-01-27 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20210126_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='File',
            field=models.ImageField(blank=True, null=True, upload_to='./static/images'),
        ),
    ]
