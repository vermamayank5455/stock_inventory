# Generated by Django 3.0.1 on 2021-01-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20210126_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./static/images/'),
        ),
    ]