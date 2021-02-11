# Generated by Django 3.0.1 on 2021-02-01 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0033_auto_20210201_1320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='size',
            new_name='invoice_no',
        ),
        migrations.AddField(
            model_name='purchase',
            name='gst',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
    ]
