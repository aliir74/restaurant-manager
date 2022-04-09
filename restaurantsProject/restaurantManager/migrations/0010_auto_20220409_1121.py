# Generated by Django 4.0.3 on 2022-04-09 11:21

from django.db import migrations


def fill_star_cnts(apps, schema_editor):
    User = apps.get_model('restaurantManager', 'User')
    Review = apps.get_model('restaurantManager', 'Review')
    for user in User.objects.all():
        user.stars_cnt = Review.objects.filter(user=user).count()
        user.save()


def fill_star_cnt_with_zero(apps, schema_editor):
    User = apps.get_model('restaurantManager', 'User')
    for user in User.objects.all():
        user.stars_cnt = 0
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantManager', '0009_user_stars_cnt'),
    ]

    operations = [
        migrations.RunPython(fill_star_cnts, reverse_code=fill_star_cnt_with_zero),
    ]