# Generated by Django 4.1.3 on 2023-03-15 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_direction_ofline_direction_online_direction_payed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direction',
            name='intramural',
        ),
    ]
