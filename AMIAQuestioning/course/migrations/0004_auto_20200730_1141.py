# Generated by Django 2.2.7 on 2020-07-30 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20200730_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motherfather',
            name='parent',
            field=models.CharField(max_length=255, verbose_name='Родитель (родные)'),
        ),
    ]
