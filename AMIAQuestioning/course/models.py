from django.db import models

no_yes_list = ['', 'нет', 'да']
yes_no_list = ['', 'да', 'нет']


# class TestKind(models.Model):
#     kind = models.CharField(max_length=255, verbose_name="Вид теста")
#
#     def __str__(self):
#         return self.kind
#
#     class Meta:
#         ordering = ('kind',)
#         verbose_name = 'Вид теста'
#         verbose_name_plural = 'Виды тестов'


class Group(models.Model):
    group_number = models.CharField(max_length=255, verbose_name='Номер группы')

    def __str__(self):
        return self.group_number

    class Meta:
        ordering = ('group_number',)
        verbose_name = 'Группа курсантов'
        verbose_name_plural = 'Группы курсантов'


class Interest(models.Model):
    interest_name = models.CharField(max_length=255, verbose_name='Интерес')

    def __str__(self):
        return self.interest_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Интерес'
        verbose_name_plural = 'Интересы'


class ParticipationInEducation(models.Model):
    participation = models.CharField(max_length=255, verbose_name='В дошкольном возрасте в '
                                                                  'вашем воспитании преимущественно принимали участие')

    def __str__(self):
        return self.participation

    class Meta:
        ordering = ('id',)
        verbose_name = 'В дошкольном возрасте в вашем воспитании преимущественно принимали участие'
        verbose_name_plural = 'В дошкольном возрасте в вашем воспитании преимущественно принимали участие'


class Relationship(models.Model):
    relationship = models.CharField(max_length=255, verbose_name='Отношение')

    def __str__(self):
        return self.relationship

    class Meta:
        ordering = ('id',)
        verbose_name = 'Отношение'
        verbose_name_plural = 'Отношения'


class ParticularQualities(models.Model):
    particular_qualities = models.CharField(max_length=255, verbose_name='Особенность')

    def __str__(self):
        return self.particular_qualities

    class Meta:
        ordering = ('id',)
        verbose_name = 'Особенность'
        verbose_name_plural = 'Особенности'


class RelativesRecord(models.Model):
    record = models.CharField(max_length=255, verbose_name='Учет у врача')

    def __str__(self):
        return self.record

    class Meta:
        ordering = ('id',)
        verbose_name = 'Учет у врача'
        verbose_name_plural = 'Учет у врача'


class Activity(models.Model):
    activity = models.CharField(max_length=255, verbose_name='Деятельность')

    def __str__(self):
        return self.activity

    class Meta:
        ordering = ('id',)
        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельности'


class Ability(models.Model):
    ability = models.CharField(max_length=255, verbose_name='Способность')

    def __str__(self):
        return self.ability

    class Meta:
        ordering = ('id',)
        verbose_name = 'Способность'
        verbose_name_plural = 'Способности'


class Messenger(models.Model):
    messenger = models.CharField(max_length=255, verbose_name='Messenger')

    def __str__(self):
        return self.messenger

    class Meta:
        ordering = ('messenger',)
        verbose_name = 'Messenger'
        verbose_name_plural = 'Messengers'


class Guardian(models.Model):
    guardian = models.CharField(max_length=255, verbose_name='Опекун')

    def __str__(self):
        return self.guardian

    class Meta:
        ordering = ('id',)
        verbose_name = 'Опекун'
        verbose_name_plural = 'Опекуны'


class MotherFather(models.Model):
    parent = models.CharField(max_length=255, verbose_name='Родитель (родные)')

    def __str__(self):
        return self.parent

    class Meta:
        ordering = ('id',)
        verbose_name = 'Родитель (родные)'
        verbose_name_plural = 'Родители (родные)'


class StepmotherStepfather(models.Model):
    step_parent = models.CharField(max_length=255, verbose_name='Родитель')

    def __str__(self):
        return self.step_parent

    class Meta:
        ordering = ('id',)
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'


class Anketa(models.Model):
    group = models.ForeignKey(Group, verbose_name="Группа", null=True, on_delete=models.SET_NULL)
    # kind = models.ForeignKey(TestKind, on_delete=models.SET_NULL, verbose_name="Вид теста", blank=True, null=True)
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    index_number = models.CharField(max_length=255, verbose_name='Порядковый номер')
    nationality = models.CharField(max_length=255, verbose_name='Национальность')
    religion = models.CharField(max_length=255, verbose_name='Вероисповедание')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    birth_place = models.TextField(verbose_name='Место рождения')
    education = models.IntegerField(verbose_name='Образование')
    year_of_graduation = models.IntegerField(verbose_name='Год окончания', blank=True, null=True)
    specialty = models.TextField(verbose_name='Специальность', blank=True, null=True)
    military = models.IntegerField(verbose_name='Служба в вооруженных силах')
    military_year_since = models.IntegerField(verbose_name='Служба в ВС с:', blank=True, null=True)
    military_year_till = models.IntegerField(verbose_name='Служба в ВС по:', blank=True, null=True)
    military_place = models.TextField(verbose_name='Место службы', blank=True, null=True)
    type_of_army = models.TextField(verbose_name='Род войск', blank=True, null=True)
    family_status = models.IntegerField(verbose_name='Семейное положение', default=1)
    marriage = models.IntegerField(verbose_name='Ранее в браке')
    marriage_year_since = models.IntegerField(verbose_name='Состоял в браке с:', blank=True, null=True)
    marriage_year_till = models.IntegerField(verbose_name='Состоял в браке по:', blank=True, null=True)
    children = models.IntegerField(verbose_name='Имеются ли у Вас дети', default=1)
    children_info = models.CharField(max_length=255, verbose_name='Пол и год рождения', blank=True, null=True)
    participation_in_education = models.ManyToManyField(ParticipationInEducation,
                                                        verbose_name='В дошкольном возрасте в вашем воспитании '
                                                                     'преимущественно принимали участие (подчеркните)')
    participation_in_education_other = models.CharField(max_length=255,
                                                        verbose_name='В дошкольном возрасте в вашем воспитании'
                                                                     ' преимущественно принимали участие (иное)', blank=True, null=True)
    parents = models.IntegerField(verbose_name='Родители на момент поступления в Академия МВД:')
    parents_in_marriage_live = models.IntegerField(verbose_name='Родители в браке проживают:', blank=True, null=True)
    parents_not_in_marriage_live = models.IntegerField(verbose_name='Родители не в браке проживают:', blank=True, null=True)
    parents_not_in_marriage_since = models.IntegerField(verbose_name='Родители не в браке проживают с:', blank=True, null=True)
    mother_only_father_died_year = models.IntegerField(verbose_name='Отец умер погиб (умер) в:', blank=True, null=True)
    mother_only_other = models.TextField(verbose_name='Только мать (иное)', blank=True, null=True)
    father_only_mother_died_year = models.IntegerField(verbose_name='Мать умерла погибла (умерла) в:', blank=True, null=True)
    father_only_other = models.TextField(verbose_name='Только отец (иное)', blank=True, null=True)
    mother_father = models.ForeignKey(MotherFather, verbose_name="Мать Отец", on_delete=models.SET_NULL, blank=True, null=True)
    stepmother_stepfather = models.ForeignKey(StepmotherStepfather, verbose_name="Мачеха Отчим", on_delete=models.SET_NULL, blank=True, null=True)
    guardian = models.ManyToManyField(Guardian, verbose_name='Опекуны', blank=True)
    guardian_other = models.CharField(max_length=255, verbose_name='Опекуны (иное)', blank=True, null=True)
    relationship = models.ManyToManyField(Relationship, verbose_name='Какие взаимоотношения преобладают между вашими родителями, лицами их заменяющими)')
    relationship_other = models.TextField(verbose_name='Взаимоотношения между родителями (иное)', blank=True, null=True)
    siblings = models.TextField(verbose_name='Братья и сестры', blank=True, null=True)
    interest = models.ManyToManyField(Interest, verbose_name='Ваши интересы, увлечения, хобби')
    interest_other = models.TextField(verbose_name='Ваши интересы (иное)', blank=True, null=True)
    kind_of_sport = models.CharField(max_length=255, verbose_name='Вид спорта', blank=True, null=True)
    sport_level = models.IntegerField(verbose_name='Уровень спорта', blank=True, null=True)
    periodicity = models.IntegerField(verbose_name='Периодичность', blank=True, null=True, default=1)
    achievements = models.TextField(verbose_name='Достижения', blank=True, null=True)
    not_prof = models.BooleanField(verbose_name='На постоянной основе спортом не занимался')

    is_chronic_diseases = models.IntegerField(verbose_name='Имеются ли хронические заболевания', default=1)
    chronic_diseases = models.TextField(verbose_name='Хронические заболевания', blank=True, null=True)
    is_injury = models.IntegerField(verbose_name='Были ли у Вас травмы, ранения, переломы и т.д.', default=1)
    injury = models.TextField(verbose_name='Травмы, ранения, переломы и т.д.', blank=True, null=True)
    particular_qualities = models.ManyToManyField(ParticularQualities, verbose_name='Отметьте свои особенности, которых вы стесняетесь, которые вас беспокоят')
    particular_qualities_other = models.TextField(verbose_name='Особенности (иные)', blank=True, null=True)
    relatives_record = models.ManyToManyField(RelativesRecord, verbose_name='Кто-либо из ваших близких родственников (родные отец, мать, бабушки, дедушки, тети, дяди)', blank=True)
    relatives_record_other = models.TextField(verbose_name='Родственники на учете у врачей(иное)', blank=True, null=True)
    level_of_wealth = models.IntegerField(verbose_name='Уровень материальной обеспеченности Вашей семьи', default=1)
    living_conditions_premises = models.IntegerField(verbose_name='ЖБУ (помещение)', default=1)
    living_conditions_premises_other = models.CharField(max_length=255, verbose_name='ЖБУ (помещение) (иное)', blank=True, null=True)
    living_conditions_room_count = models.IntegerField(verbose_name='ЖБУ (число комнат)', default=1)
    living_conditions_people_count = models.IntegerField(verbose_name='ЖБУ (число проживающих людей)', default=1)
    is_own_room = models.IntegerField(verbose_name='Имеется ли у Вас отдельная комната', default=1)

    activity = models.ManyToManyField(Activity, verbose_name='Деятельность, в которой Вы бы хотели себя реализовать')
    activity_other = models.TextField(verbose_name='Деятельность, в которой Вы бы хотели себя реализовать(иное)', blank=True, null=True)
    ability = models.ManyToManyField(Ability, verbose_name='Какими способностями Вы обладаете')
    ability_other = models.TextField(verbose_name='Какими способностями Вы обладаете(иное)', blank=True, null=True)
    gaming = models.IntegerField(verbose_name='Как часто Вы играли в компьютерные игры в последнее время', default=1)
    gaming_hours = models.IntegerField(verbose_name='Как часто Вы играли в компьютерные игры в последнее время - часов', blank=True, null=True)
    friends_count = models.IntegerField(verbose_name='Количество постоянных друзей в повседневной жизни', default=2)
    messenger = models.ManyToManyField(Messenger, verbose_name='Какие мессенджеры / мобильные приложения предпочитаете для общения?')
    messenger_other = models.TextField(verbose_name='Messenger', blank=True, null=True)
    smoking = models.IntegerField(verbose_name='Курите ли Вы', default=1)
    smoking_try_in_year = models.IntegerField(verbose_name='Впервые попробовал курить в __ лет', blank=True, null=True)
    smoking_beginning_in_year = models.IntegerField(verbose_name='Начал курить в __ лет', blank=True, null=True)
    smoking_ending_in_year = models.IntegerField(verbose_name='Бросил курить в __ лет', blank=True, null=True)
    if_had_not_entered = models.TextField(verbose_name='Если бы не поступил, специальность по которой хотел бы работать', default="")

    def __str__(self):
        return self.fio

    @property
    def get_education(self):
        education_list = ['', 'общее среднее (школа на базе 11 классов, лицей)', 'среднее профессиональное (ПТУ, лицей МВД (МЧС), кадетское, Суворовское)',
                          'среднее-специальное (техникум, колледж, лицей)']
        return education_list[self.education]

    @property
    def get_military(self):
        military_list = ['', 'не служил', 'служил']
        return military_list[self.military]

    @property
    def get_family_status(self):
        family_status_list = ['', 'Холост', 'Не замужем', 'Женат', 'Замужем', 'Разведен(а)', 'Вдовец', 'Вдова']
        return family_status_list[self.family_status]

    @property
    def get_marriage(self):
        marriage_list = ['','не состоял', 'состоял']
        return marriage_list[self.marriage]

    @property
    def get_children(self):
        return no_yes_list[self.children]

    @property
    def get_parents(self):
        parent_status_id = self.parents
        parent_status = ''
        if parent_status_id == 1:
            parent_status = 'Мать и отец родные, состоят в браке, проживают '
            if self.parents_in_marriage_live == 1:
                parent_status += 'совместно'
            else:
                parent_status += 'раздельно'
        elif parent_status_id == 2:
            parent_status = 'Мать и отец родные, находятся в разводе с '
            parent_status += str(self.parents_not_in_marriage_since)
            parent_status += ' проживают '
            if self.parents_not_in_marriage_live == 1:
                parent_status += 'совместно'
            else:
                parent_status += 'раздельно'
        elif parent_status_id == 3:
            parent_status += 'Родная (-ой) '
            if self.mother_father == 1:
                parent_status += 'мать '
            else:
                parent_status += 'отец '
            parent_status += 'проживает совместно с '
            if self.stepmother_stepfather == 1:
                parent_status += 'отчимом '
            else:
                parent_status += 'мачехой '
            parent_status += 'в браке'
        elif parent_status_id == 4:
            parent_status += 'Родная (-ой) '
            if self.mother_father == 1:
                parent_status += 'мать '
            else:
                parent_status += 'отец '
            parent_status += 'проживает совместно с '
            if self.stepmother_stepfather == 1:
                parent_status += 'отчимом '
            else:
                parent_status += 'мачехой '
            parent_status += 'без регистрации брака'
        elif parent_status_id == 5:
            parent_status += 'Только мать, так как отец умер (погиб) в '
            parent_status += str(self.mother_only_father_died_year)
            parent_status += ' году, иное '
            parent_status += str(self.mother_only_other)
        elif parent_status_id == 6:
            parent_status += 'Только отец, мать умерла (погибла) в '
            parent_status += str(self.father_only_mother_died_year)
            parent_status += ' году, иное '
            parent_status += str(self.father_only_other)
        elif parent_status_id == 7:
            parent_status += 'Опекуны: '
            for guardian in self.guardian.all():
                parent_status += guardian.guardian
                parent_status += ', '
            if self.guardian_other:
                parent_status += str(self.guardian_other)
        elif parent_status_id == 8:
            parent_status += 'Приемные родители, состоят в браке, проживают совместно'
        elif parent_status_id == 9:
            parent_status += 'Воспитанник детского дома'
        return parent_status

    @property
    def get_sport_level(self):
        if self.sport_level:
            sport_level_list = ['', 'на любительском уровне', 'профессионально']
            return sport_level_list[self.sport_level]
        else:
            return ''

    @property
    def get_sport_periodicity(self):
        sport_periodicity_list = ['', '1', '2', '3', '4', '5', '6', 'Ежедневно']
        if self.periodicity != 7:
            if self.periodicity in [2, 3, 4]:
                periodicity = str(sport_periodicity_list[self.periodicity]) + ' дня в неделю'
            elif self.periodicity == 1:
                periodicity = str(sport_periodicity_list[self.periodicity]) + ' день в неделю'
            else:
                periodicity = str(sport_periodicity_list[self.periodicity]) + ' дней в неделю'
        else:
            periodicity = str(sport_periodicity_list[self.periodicity])
        return periodicity

    @property
    def get_not_prof(self):
        return 'Не занимался' if self.not_prof else 'Занимался'

    @property
    def get_is_chronic_diseases(self):
        return no_yes_list[self.is_chronic_diseases]

    @property
    def get_is_injury(self):
        return no_yes_list[self.is_injury]

    @property
    def get_level_of_wealth(self):
        level_of_wealth_list = ['', 'высокая', 'выше средней', 'средняя', 'ниже средней', 'низкая']
        return level_of_wealth_list[self.level_of_wealth]

    @property
    def get_living_conditions_premises(self):
        living_conditions_premises_list = ['', 'Квартира', 'Частный дом', 'Комната (блок) в общежитии', 'Иное']
        return living_conditions_premises_list[self.living_conditions_premises]

    @property
    def get_living_conditions_room_count(self):
        living_conditions_room_count_list = ['', '1', '2', '3', '4', '5 и более']
        return living_conditions_room_count_list[self.living_conditions_room_count]

    @property
    def get_living_conditions_people_count(self):
        living_conditions_people_count_list = ['', '1', '2', '3', '4', '5 и более']
        return living_conditions_people_count_list[self.living_conditions_people_count]

    @property
    def get_is_own_room(self):
        return yes_no_list[self.is_own_room]

    @property
    def get_gaming(self):
        gaming_id = self.gaming
        gaming = ''
        if gaming_id == 1:
            gaming += 'не играл(а)'
        elif gaming_id == 2:
            gaming += 'не более 2 раз в неделю'
        elif gaming_id == 3:
            gaming += '3-5 раз в неделю по '
            if self.gaming_hours:
                gaming += str(self.gaming_hours)
            else:
                gaming += '-'
            gaming += ' часа(-ов)'
        elif gaming_id == 4:
            gaming += 'ежедневно по '
            if self.gaming_hours:
                gaming += str(self.gaming_hours)
            else:
                gaming += '-'
            gaming += ' часа(-ов)'
        return gaming

    def get_smoking(self):
        smoking_id = self.smoking
        smoking = ''
        if smoking_id == 1:
            smoking += 'не курю и никогда не курил'
        elif smoking_id == 2:
            smoking += 'не курю, но впервые попробовал в '
            smoking += str(self.smoking_try_in_year)
            smoking += ' лет'
        elif smoking_id == 3:
            smoking += 'курил с '
            smoking += str(self.smoking_beginning_in_year)
            smoking += ' лет, бросил в '
            smoking += str(self.smoking_ending_in_year)
            smoking += ' году'
        elif smoking_id == 4:
            smoking += 'курю иногда (периодически) с '
            smoking += str(self.smoking_beginning_in_year)
            smoking += ' лет'
        elif smoking_id == 5:
            smoking += 'курю постоянно с '
            smoking += str(self.smoking_beginning_in_year)
            smoking += ' лет'
        return smoking

    class Meta:
        ordering = ('id',)
        verbose_name = 'Анкета первокурсника'
        verbose_name_plural = 'Анкеты первокурсников'