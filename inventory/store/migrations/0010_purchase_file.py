# Generated by Django 3.0.1 on 2021-01-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210122_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='File',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
