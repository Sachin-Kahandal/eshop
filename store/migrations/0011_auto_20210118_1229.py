# Generated by Django 3.1.4 on 2021-01-18 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20210118_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(),
        ),
    ]