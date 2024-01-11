# Generated by Django 5.0.1 on 2024-01-10 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_from', models.CharField(blank=True, max_length=100, null=True)),
                ('local_id', models.PositiveIntegerField(blank=True, null=True)),
                ('share_id', models.PositiveIntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_from', models.CharField(blank=True, max_length=100, null=True)),
                ('local_id', models.PositiveIntegerField(blank=True, null=True)),
                ('share_id', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price', to='price.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
