# Generated by Django 3.1.4 on 2021-01-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210117_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='Pune', max_length=100),
        ),
    ]
