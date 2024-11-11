# Generated by Django 5.1.2 on 2024-11-08 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventoryId', models.AutoField(primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('category', models.CharField(choices=[('Food', 'Food'), ('Toys', 'Toys'), ('Fur Clothing', 'Fur Clothing'), ('Care Products', 'Care Products')], max_length=50, null=True)),
                ('price', models.PositiveBigIntegerField(null=True)),
                ('inventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_page.inventory')),
            ],
        ),
    ]