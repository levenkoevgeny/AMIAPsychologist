# Generated by Django 2.2.7 on 2021-02-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adaptation', '0002_auto_20210217_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adaptation',
            name='average_score',
            field=models.FloatField(verbose_name='26. Средний балл по итогам первой сессии'),
        ),
        migrations.AlterField(
            model_name='adaptation',
            name='date_added',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата заполнения'),
        ),
        migrations.AlterField(
            model_name='adaptation',
            name='tension',
            field=models.ManyToManyField(blank=True, to='adaptation.Tension', verbose_name='51. Что вызывает у Вас наибольшее напряжение, неудовлетворенность'),
        ),
    ]
