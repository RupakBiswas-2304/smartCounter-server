# Generated by Django 4.0.4 on 2022-04-13 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_house_authtoken_alter_house_total_device_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.house'),
        ),
        migrations.AlterField(
            model_name='room',
            name='present_in',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='total_device',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='total_in',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='total_out',
            field=models.IntegerField(default=0),
        ),
    ]
