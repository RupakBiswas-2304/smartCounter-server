# Generated by Django 4.0.4 on 2022-04-13 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_device_house_alter_room_present_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='mac_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
