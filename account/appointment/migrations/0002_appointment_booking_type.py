# Generated by Django 5.1.2 on 2024-11-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='booking_type',
            field=models.CharField(choices=[('grooming', 'Grooming'), ('boarding', 'Boarding')], default='grooming', max_length=20),
            preserve_default=False,
        ),
    ]
