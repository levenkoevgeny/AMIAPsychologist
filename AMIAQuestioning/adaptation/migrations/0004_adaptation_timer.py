# Generated by Django 2.2.7 on 2021-02-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adaptation', '0003_auto_20210217_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='adaptation',
            name='timer',
            field=models.IntegerField(blank=True, null=True, verbose_name='Таймер'),
        ),
    ]
