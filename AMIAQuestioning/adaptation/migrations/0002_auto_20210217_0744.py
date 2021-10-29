# Generated by Django 2.2.7 on 2021-02-17 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adaptation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tension',
            options={'ordering': ('id',), 'verbose_name': 'Напряжение', 'verbose_name_plural': 'Напряжения'},
        ),
        migrations.AddField(
            model_name='adaptation',
            name='tension_other',
            field=models.TextField(blank=True, null=True, verbose_name='51_1. Что вызывает у Вас наибольшее напряжение, неудовлетворенность (иное)'),
        ),
    ]