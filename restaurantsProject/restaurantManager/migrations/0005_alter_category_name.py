# Generated by Django 4.0.3 on 2022-04-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantManager', '0004_alter_restaurant_attributes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
