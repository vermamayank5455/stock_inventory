# Generated by Django 3.0.1 on 2021-02-01 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0032_auto_20210130_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='address',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='date',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='price',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='size',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='vendor',
        ),
    ]
