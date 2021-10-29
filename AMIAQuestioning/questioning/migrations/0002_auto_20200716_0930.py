# Generated by Django 2.2.7 on 2020-07-16 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questioning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionary',
            name='decision_other',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Решение о поступлении на обучение было принято (иное)'),
        ),
        migrations.AddField(
            model_name='questionary',
            name='got_information_from_other',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Информацию о поступлении в Академия получил (иное)'),
        ),
        migrations.AddField(
            model_name='questionary',
            name='important_for_other',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='При выборе высшего УО важно (иное)'),
        ),
        migrations.AddField(
            model_name='questionary',
            name='in_the_interests_of_other',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='На учебу в Академию МВД Вы направляетесь (иное)'),
        ),
    ]
