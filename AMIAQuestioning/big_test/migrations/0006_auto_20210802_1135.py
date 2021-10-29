# Generated by Django 2.2.7 on 2021-08-02 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('big_test', '0005_questionary_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=255, verbose_name='Вид теста')),
            ],
            options={
                'verbose_name': 'Вид теста',
                'verbose_name_plural': 'Виды тестов',
                'ordering': ('kind',),
            },
        ),
        migrations.AlterField(
            model_name='questionary',
            name='kind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='big_test.TestKind', verbose_name='Вид теста'),
        ),
    ]