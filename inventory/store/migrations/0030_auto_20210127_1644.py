# Generated by Django 3.0.1 on 2021-01-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_auto_20210127_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]