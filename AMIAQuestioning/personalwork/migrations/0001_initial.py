# Generated by Django 2.2.7 on 2021-10-25 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_title', models.CharField(max_length=255, verbose_name='Звание')),
            ],
            options={
                'verbose_name': 'Звание',
                'verbose_name_plural': 'Звания',
                'ordering': ('rank_title',),
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_request', models.CharField(max_length=255, verbose_name='Запрос')),
            ],
            options={
                'verbose_name': 'Запрос',
                'verbose_name_plural': 'Запросы',
                'ordering': ('work_request',),
            },
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subdivision_title', models.CharField(max_length=255, verbose_name='Подразделение')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Подразделения',
                'ordering': ('subdivision_title',),
            },
        ),
        migrations.CreateModel(
            name='WorkDone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_done', models.CharField(max_length=255, verbose_name='Основание и проведенная работа')),
            ],
            options={
                'verbose_name': 'Основание и проведенная работа',
                'verbose_name_plural': 'Основания и проведенные работы',
                'ordering': ('work_done',),
            },
        ),
        migrations.CreateModel(
            name='WorkKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_kind', models.CharField(max_length=255, verbose_name='Вид работы')),
            ],
            options={
                'verbose_name': 'Вид работы',
                'verbose_name_plural': 'Виды работы',
                'ordering': ('work_kind',),
            },
        ),
        migrations.CreateModel(
            name='PersonalWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=255, verbose_name='Фамилия и инициалы')),
                ('work_date', models.DateField(verbose_name='Дата')),
                ('conclusion', models.TextField(blank=True, null=True, verbose_name='Выводы')),
                ('recommendations', models.TextField(blank=True, null=True, verbose_name='Рекомендации')),
                ('add_date_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления записи')),
                ('last_modification', models.DateTimeField(auto_now=True, verbose_name='Дата и время последнего редактирования')),
                ('extra_data', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
                ('rank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personalwork.Rank', verbose_name='Звание')),
                ('subdivision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalwork.Subdivision', verbose_name='Подразделение')),
                ('work_done', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalwork.WorkDone', verbose_name='Основание и проведеннная работа')),
                ('work_kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalwork.WorkKind', verbose_name='Вид работы')),
                ('work_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalwork.Request', verbose_name='Запрос')),
            ],
            options={
                'verbose_name': 'Персональная работа',
                'verbose_name_plural': 'Персональные работы',
                'ordering': ('-work_date', '-id'),
            },
        ),
    ]
