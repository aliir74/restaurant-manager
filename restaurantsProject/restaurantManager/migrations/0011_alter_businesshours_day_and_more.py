# Generated by Django 4.0.3 on 2022-04-09 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantManager', '0010_auto_20220409_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesshours',
            name='day',
            field=models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], max_length=10),
        ),
        migrations.AlterField(
            model_name='businesshours',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_hours', to='restaurantManager.restaurant'),
        ),
        migrations.AlterField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='restaurantManager.restaurant'),
        ),
    ]