# Generated by Django 3.0.1 on 2021-01-12 05:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('pno', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=200)),
                ('vendor', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('size', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_no', models.AutoField(primary_key=True, serialize=False)),
                ('vendor', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('size', models.IntegerField()),
                ('address', models.TextField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Stock')),
            ],
        ),
    ]