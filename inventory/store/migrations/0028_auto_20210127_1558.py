# Generated by Django 3.0.1 on 2021-01-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_auto_20210127_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='../static/images'),
        ),
    ]
