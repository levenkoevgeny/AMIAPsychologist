# Generated by Django 2.2.7 on 2020-12-22 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graduate', '0002_auto_20201221_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowDidLeadersInfluence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_did_leaders_influence', models.CharField(max_length=255, verbose_name='Как в целом повлияли на ваше профессиональное становление курсовые офицеры?')),
            ],
            options={
                'verbose_name': 'Как повлияли курсовые',
                'verbose_name_plural': 'Как повлияли курсовые',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='HowDidTeachersInfluence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_did_teachers_influence', models.CharField(max_length=255, verbose_name='Как в целом повлияли на ваше профессиональное становление преподаватели Академии МВД?')),
            ],
            options={
                'verbose_name': 'Как повлияли преподаватели',
                'verbose_name_plural': 'Как повлияли преподаватели',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='WhatInduceToQuit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_induce_to_quit', models.CharField(max_length=255, verbose_name='Что может побудить Вас уволиться?')),
            ],
            options={
                'verbose_name': 'Что может побудить уволиться',
                'verbose_name_plural': 'Что может побудить уволиться',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='WhatKeeps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_keeps', models.CharField(max_length=255, verbose_name='Что Вас удерживает или мотивирует продолжать службу?')),
            ],
            options={
                'verbose_name': 'Что удерживает',
                'verbose_name_plural': 'Что удерживает',
                'ordering': ('id',),
            },
        ),
        migrations.RemoveField(
            model_name='graduateform',
            name='what_taught',
        ),
        migrations.AddField(
            model_name='graduateform',
            name='how_did_leaders_influence_explain',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Как в целом повлияли на ваше профессиональное становление курсовые офицеры? (поясните ответ)'),
        ),
        migrations.AddField(
            model_name='graduateform',
            name='how_did_teachers_influence_explain',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Как в целом повлияли на ваше профессиональное становление преподаватели Академии МВД? (поясните ответ)'),
        ),
        migrations.AddField(
            model_name='graduateform',
            name='what_induce_to_quit_other',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Что может побудить Вас уволиться? (иное)'),
        ),
        migrations.AddField(
            model_name='graduateform',
            name='what_keeps_other',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Что Вас удерживает или мотивирует продолжать службу? (иное)'),
        ),
        migrations.AddField(
            model_name='graduateform',
            name='how_did_leaders_influence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='graduate.HowDidLeadersInfluence', verbose_name='Как в целом повлияли на ваше профессиональное становление курсовые офицеры?'),
        ),
        migrations.AddField(
            model_name='graduateform',
            name='how_did_teachers_influence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='graduate.HowDidTeachersInfluence', verbose_name='Как в целом повлияли на ваше профессиональное становление преподаватели Академии МВД?'),
        ),
        migrations.AddField(
            model_name='graduateform',
            name='what_induce_to_quit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='graduate.WhatInduceToQuit', verbose_name='Что может побудить Вас уволиться?'),
        ),
        migrations.AddField(
            model_name='graduateform',
            name='what_keeps',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='graduate.WhatKeeps', verbose_name='Что Вас удерживает или мотивирует продолжать службу?'),
        ),
    ]
