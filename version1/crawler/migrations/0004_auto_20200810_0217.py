# Generated by Django 3.0.8 on 2020-08-09 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0003_productinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='price',
            field=models.CharField(max_length=150),
        ),
    ]