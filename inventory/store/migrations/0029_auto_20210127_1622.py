# Generated by Django 3.0.1 on 2021-01-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_auto_20210127_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
