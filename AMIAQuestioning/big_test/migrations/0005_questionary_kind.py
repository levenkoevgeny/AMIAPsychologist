# Generated by Django 2.2.7 on 2021-08-02 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_remove_anketa_kind'),
        ('big_test', '0004_auto_20210729_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionary',
            name='kind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.TestKind', verbose_name='Вид теста'),
        ),
    ]
