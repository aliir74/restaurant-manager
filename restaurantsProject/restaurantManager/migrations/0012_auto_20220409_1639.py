# Generated by Django 4.0.3 on 2022-04-09 16:39

from django.db import migrations


map = {
    '1': 'Mon',
    '2': 'Tue',
    '3': 'Wed',
    '4': 'Thu',
    '5': 'Fri',
    '6': 'Sat',
    '7': 'Sun'
}


def map_number_to_str_for_days(apps, schema_editor):
    BusinessHour = apps.get_model('restaurantManager', 'BusinessHours')
    for bh in BusinessHour.objects.all():
        bh.day = map[bh.day]
        bh.save()


def map_str_to_number_for_days(apps, schema_editor):
    BusinessHour = apps.get_model('restaurantManager', 'BusinessHours')
    reverse_map = {v: k for k, v in map.items()}
    for bh in BusinessHour.objects.all():
        bh.day = reverse_map[bh.day]
        bh.save()


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantManager', '0011_alter_businesshours_day_and_more'),
    ]

    operations = [
        migrations.RunPython(map_number_to_str_for_days, reverse_code=map_str_to_number_for_days),
    ]