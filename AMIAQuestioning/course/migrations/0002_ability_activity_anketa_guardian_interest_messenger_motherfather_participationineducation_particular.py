# Generated by Django 2.2.7 on 2020-07-30 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability', models.CharField(max_length=255, verbose_name='Способность')),
            ],
            options={
                'verbose_name': 'Способность',
                'verbose_name_plural': 'Способности',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=255, verbose_name='Деятельность')),
            ],
            options={
                'verbose_name': 'Деятельность',
                'verbose_name_plural': 'Деятельности',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guardian', models.CharField(max_length=255, verbose_name='Опекун')),
            ],
            options={
                'verbose_name': 'Опекун',
                'verbose_name_plural': 'Опекуны',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_name', models.CharField(max_length=255, verbose_name='Интерес')),
            ],
            options={
                'verbose_name': 'Интерес',
                'verbose_name_plural': 'Интересы',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Messenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messenger', models.CharField(max_length=255, verbose_name='Messenger')),
            ],
            options={
                'verbose_name': 'Messenger',
                'verbose_name_plural': 'Messengers',
                'ordering': ('messenger',),
            },
        ),
        migrations.CreateModel(
            name='MotherFather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.CharField(max_length=255, verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Родитель',
                'verbose_name_plural': 'Родители',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ParticipationInEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participation', models.CharField(max_length=255, verbose_name='В дошкольном возрасте в вашем воспитании преимущественно принимали участие')),
            ],
            options={
                'verbose_name': 'В дошкольном возрасте в вашем воспитании преимущественно принимали участие',
                'verbose_name_plural': 'В дошкольном возрасте в вашем воспитании преимущественно принимали участие',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ParticularQualities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particular_qualities', models.CharField(max_length=255, verbose_name='Особенность')),
            ],
            options={
                'verbose_name': 'Особенность',
                'verbose_name_plural': 'Особенности',
                'ordering': ('particular_qualities',),
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(max_length=255, verbose_name='Отношение')),
            ],
            options={
                'verbose_name': 'Отношение',
                'verbose_name_plural': 'Отношения',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='RelativesRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.CharField(max_length=255, verbose_name='Учет у врача')),
            ],
            options={
                'verbose_name': 'Учет у врача',
                'verbose_name_plural': 'Учет у врача',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='StepmotherStepfather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_parent', models.CharField(max_length=255, verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Родитель',
                'verbose_name_plural': 'Родители',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Anketa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, verbose_name='ФИО')),
                ('index_number', models.CharField(max_length=255, verbose_name='Порядковый номер')),
                ('nationality', models.CharField(max_length=255, verbose_name='Национальность')),
                ('religion', models.CharField(max_length=255, verbose_name='Вероисповедание')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('birth_place', models.TextField(verbose_name='Место рождения')),
                ('education', models.IntegerField(verbose_name='Образование')),
                ('year_of_graduation', models.IntegerField(verbose_name='Год окончания')),
                ('specialty', models.TextField(blank=True, null=True, verbose_name='Специальность')),
                ('military', models.IntegerField(verbose_name='Служба в вооруженных силах')),
                ('military_year_since', models.IntegerField(blank=True, null=True, verbose_name='Служба в ВС с:')),
                ('military_year_till', models.IntegerField(blank=True, null=True, verbose_name='Служба в ВС по:')),
                ('military_place', models.TextField(blank=True, null=True, verbose_name='Место службы')),
                ('type_of_army', models.TextField(blank=True, null=True, verbose_name='Род войск')),
                ('family_status', models.IntegerField(default=1, verbose_name='Семейное положение')),
                ('marriage', models.IntegerField(verbose_name='Ранее в браке')),
                ('marriage_year_since', models.IntegerField(blank=True, null=True, verbose_name='Состоял в браке с:')),
                ('marriage_year_till', models.IntegerField(blank=True, null=True, verbose_name='Состоял в браке по:')),
                ('children', models.IntegerField(default=1, verbose_name='Имеются ли у Вас дети')),
                ('children_info', models.CharField(blank=True, max_length=255, null=True, verbose_name='Пол и год рождения')),
                ('participation_in_education_other', models.CharField(blank=True, max_length=255, null=True, verbose_name='В дошкольном возрасте в вашем воспитании преимущественно принимали участие (иное)')),
                ('parents', models.IntegerField(verbose_name='Родители на момент поступления в Академия МВД:')),
                ('parents_in_marriage_live', models.IntegerField(blank=True, null=True, verbose_name='Родители в браке проживают:')),
                ('parents_not_in_marriage_live', models.IntegerField(blank=True, null=True, verbose_name='Родители не в браке проживают:')),
                ('parents_not_in_marriage_since', models.IntegerField(blank=True, null=True, verbose_name='Родители не в браке проживают с:')),
                ('mother_only_father_died_year', models.IntegerField(blank=True, null=True, verbose_name='Отец умер погиб (умер) в:')),
                ('mother_only_other', models.TextField(blank=True, null=True, verbose_name='Только мать (иное)')),
                ('father_only_mother_died_year', models.IntegerField(blank=True, null=True, verbose_name='Мать умерла погибла (умерла) в:')),
                ('father_only_other', models.TextField(blank=True, null=True, verbose_name='Только отец (иное)')),
                ('guardian_other', models.CharField(blank=True, max_length=255, null=True, verbose_name='Опекуны (иное)')),
                ('relationship_other', models.TextField(blank=True, null=True, verbose_name='Взаимоотношения между родителями (иное)')),
                ('siblings', models.TextField(blank=True, null=True, verbose_name='Братья и сестры')),
                ('interest_other', models.TextField(blank=True, null=True, verbose_name='Ваши интересы (иное)')),
                ('kind_of_sport', models.CharField(blank=True, max_length=255, null=True, verbose_name='Вид спорта')),
                ('sport_level', models.IntegerField(blank=True, null=True, verbose_name='Уровень спорта')),
                ('periodicity', models.IntegerField(blank=True, default=1, null=True, verbose_name='Периодичность')),
                ('achievements', models.TextField(blank=True, null=True, verbose_name='Достижения')),
                ('not_prof', models.BooleanField(verbose_name='На постоянной основе спортом не занимался')),
                ('is_chronic_diseases', models.IntegerField(default=1, verbose_name='Имеются ли хронические заболевания')),
                ('chronic_diseases', models.TextField(blank=True, null=True, verbose_name='Хронические заболевания')),
                ('is_injury', models.IntegerField(default=1, verbose_name='Были ли у Вас травмы, ранения, переломы и т.д.')),
                ('injury', models.TextField(blank=True, null=True, verbose_name='Травмы, ранения, переломы и т.д.')),
                ('particular_qualities_other', models.TextField(blank=True, null=True, verbose_name='Особенности (иные)')),
                ('relatives_record_other', models.TextField(blank=True, null=True, verbose_name='Родственники на учете у врачей(иное)')),
                ('level_of_wealth', models.IntegerField(default=1, verbose_name='Уровень материальной обеспеченности Вашей семьи')),
                ('living_conditions_premises', models.IntegerField(default=1, verbose_name='ЖБУ (помещение)')),
                ('living_conditions_premises_other', models.CharField(blank=True, max_length=255, null=True, verbose_name='ЖБУ (помещение) (иное)')),
                ('living_conditions_room_count', models.IntegerField(default=1, verbose_name='ЖБУ (число комнат)')),
                ('living_conditions_people_count', models.IntegerField(default=1, verbose_name='ЖБУ (число проживающих людей)')),
                ('is_own_room', models.IntegerField(default=1, verbose_name='Имеется ли у Вас отдельная комната')),
                ('activity_other', models.TextField(blank=True, null=True, verbose_name='Деятельность, в которой Вы бы хотели себя реализовать(иное)')),
                ('ability_other', models.TextField(blank=True, null=True, verbose_name='Какими способностями Вы обладаете(иное)')),
                ('gaming', models.IntegerField(default=1, verbose_name='Как часто Вы играли в компьютерные игры в последнее время')),
                ('gaming_hours', models.IntegerField(blank=True, null=True, verbose_name='Как часто Вы играли в компьютерные игры в последнее время - часов')),
                ('friends_count', models.IntegerField(default=2, verbose_name='Количество постоянных друзей в повседневной жизни')),
                ('messenger_other', models.TextField(blank=True, null=True, verbose_name='Messenger')),
                ('smoking', models.IntegerField(default=1, verbose_name='Курите ли Вы')),
                ('smoking_try_in_year', models.IntegerField(blank=True, null=True, verbose_name='Впервые попробовал курить в __ лет')),
                ('smoking_beginning_in_year', models.IntegerField(blank=True, null=True, verbose_name='Начал курить в __ лет')),
                ('smoking_ending_in_year', models.IntegerField(blank=True, null=True, verbose_name='Бросил курить в __ лет')),
                ('if_had_not_entered', models.TextField(default='', verbose_name='Если бы не поступил, специальность по которой хотел бы работать')),
                ('ability', models.ManyToManyField(to='course.Ability', verbose_name='Какими способностями Вы обладаете')),
                ('activity', models.ManyToManyField(to='course.Activity', verbose_name='Деятельность, в которой Вы бы хотели себя реализовать')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.Group', verbose_name='Группа')),
                ('guardian', models.ManyToManyField(blank=True, to='course.Guardian', verbose_name='Опекун')),
                ('interest', models.ManyToManyField(to='course.Interest', verbose_name='Ваши интересы, увлечения, хобби')),
                ('messenger', models.ManyToManyField(to='course.Messenger', verbose_name='Messenger')),
                ('mother_father', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.MotherFather')),
                ('participation_in_education', models.ManyToManyField(to='course.ParticipationInEducation', verbose_name='В дошкольном возрасте в вашем воспитании преимущественно принимали участие (подчеркните)')),
                ('particular_qualities', models.ManyToManyField(to='course.ParticularQualities', verbose_name='Особенности')),
                ('relationship', models.ManyToManyField(to='course.Relationship', verbose_name='Взаимоотношения между родителями')),
                ('relatives_record', models.ManyToManyField(to='course.RelativesRecord', verbose_name='Родственники на учете у врачей')),
                ('stepmother_stepfather', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.StepmotherStepfather')),
            ],
            options={
                'verbose_name': 'Анкета первокурсника',
                'verbose_name_plural': 'Анкеты первокурсников',
                'ordering': ('id',),
            },
        ),
    ]
