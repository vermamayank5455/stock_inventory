# Generated by Django 3.0.1 on 2021-02-01 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0034_auto_20210201_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='hsn',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]