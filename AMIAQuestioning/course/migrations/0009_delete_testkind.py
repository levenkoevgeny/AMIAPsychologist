# Generated by Django 2.2.7 on 2021-08-02 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('big_test', '0006_auto_20210802_1135'),
        ('course', '0008_remove_anketa_kind'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestKind',
        ),
    ]
