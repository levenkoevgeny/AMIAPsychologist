from django.db import models


class Rank(models.Model):
    rank = models.CharField(max_length=100, verbose_name="Специальное звание")

    def __str__(self):
        return self.rank

    class Meta:
        ordering = ('id',)
        verbose_name = 'Специальное звание'
        verbose_name_plural = 'Специальные звания'


class Position(models.Model):
    position = models.CharField(max_length=255, verbose_name="Должность")

    def __str__(self):
        return self.position

    class Meta:
        ordering = ('id',)
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Guardian(models.Model):
    guardian = models.CharField(max_length=255, verbose_name="Опекун")

    def __str__(self):
        return self.guardian

    class Meta:
        ordering = ('id',)
        verbose_name = 'Опекун'
        verbose_name_plural = 'Опекуны'


class SatisfiedWithTheTraining(models.Model):
    satisfied = models.CharField(max_length=255, verbose_name="Удотволерены ли Вы как прошло обучение")

    def __str__(self):
        return self.satisfied

    class Meta:
        ordering = ('id',)
        verbose_name = 'Удовлетворение обучением'
        verbose_name_plural = 'Удовлетворение обучением'


class Expectations(models.Model):
    expectation = models.CharField(max_length=255, verbose_name="Ожидание")

    def __str__(self):
        return self.expectation

    class Meta:
        ordering = ('id',)
        verbose_name = 'Оправдание ожиданий'
        verbose_name_plural = 'Оправдание ожиданий'


class CharacterChange(models.Model):
    change = models.CharField(max_length=255, verbose_name="Изменение")

    def __str__(self):
        return self.change

    class Meta:
        ordering = ('id',)
        verbose_name = 'Изменение характера'
        verbose_name_plural = 'Изменение характера'


class AfterGraduating(models.Model):
    after_graduating = models.CharField(max_length=255, verbose_name="Действия после окончания Академии")

    def __str__(self):
        return self.after_graduating

    class Meta:
        ordering = ('id',)
        verbose_name = 'Действие после окончания'
        verbose_name_plural = 'Действия после окончания'


class WhatInduceToQuit(models.Model):
    what_induce_to_quit = models.CharField(max_length=255, verbose_name="Что может побудить Вас уволиться?")

    def __str__(self):
        return self.what_induce_to_quit

    class Meta:
        ordering = ('id',)
        verbose_name = 'Что может побудить уволиться'
        verbose_name_plural = 'Что может побудить уволиться'


class WhatKeeps(models.Model):
    what_keeps = models.CharField(max_length=255, verbose_name="Что Вас удерживает или мотивирует продолжать службу?")

    def __str__(self):
        return self.what_keeps

    class Meta:
        ordering = ('id',)
        verbose_name = 'Что удерживает'
        verbose_name_plural = 'Что удерживает'


class HowDidTeachersInfluence(models.Model):
    how_did_teachers_influence = models.CharField(max_length=255, verbose_name="Как в целом повлияли на ваше профессиональное становление преподаватели Академии МВД?")

    def __str__(self):
        return self.how_did_teachers_influence

    class Meta:
        ordering = ('id',)
        verbose_name = 'Как повлияли преподаватели'
        verbose_name_plural = 'Как повлияли преподаватели'


class HowDidLeadersInfluence(models.Model):
    how_did_leaders_influence = models.CharField(max_length=255, verbose_name="Как в целом повлияли на ваше профессиональное становление курсовые офицеры?")

    def __str__(self):
        return self.how_did_leaders_influence

    class Meta:
        ordering = ('id',)
        verbose_name = 'Как повлияли курсовые'
        verbose_name_plural = 'Как повлияли курсовые'


class Inform(models.Model):
    i_inform = models.CharField(max_length=255, verbose_name="Я информирован - по психологической помощи")

    def __str__(self):
        return self.i_inform

    class Meta:
        ordering = ('id',)
        verbose_name = 'Информирован'
        verbose_name_plural = 'Информирован'


class GraduateForm(models.Model):
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, verbose_name="Специальное звание")
    group = models.CharField(max_length=100, verbose_name="Группа")
    fio = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Должность")
    marital_status = models.IntegerField(verbose_name="Семейное положение")
    married_from = models.IntegerField(verbose_name="Женат/замужем с - ", blank=True, null=True)
    has_children = models.IntegerField(verbose_name="Имеются ли дети?", default=0)
    children_data = models.CharField(max_length=255, verbose_name="Пол и год рождения ребенка",
                                     blank=True, null=True)
    parents_data = models.IntegerField(verbose_name="Сведения о родителях")
    divorced_from = models.IntegerField(verbose_name="В разводе с", blank=True, null=True)
    divorced_live = models.IntegerField(verbose_name="В разводе - живут", blank=True, null=True)
    mother_only_father_died_in = models.IntegerField(verbose_name="Отец умер(погиб) в", blank=True, null=True)
    mother_only_father_died_other = models.CharField(max_length=255, verbose_name="Отец умер(погиб) иное",
                                                     blank=True, null=True)
    father_only_mother_died_in = models.IntegerField(verbose_name="Мать умерла(погибла) в", blank=True, null=True)
    father_only_mother_died_other = models.CharField(max_length=255, verbose_name="Мать умерла(погибла) иное",
                                                     blank=True, null=True)
    stepfather_stepmother_marriage_mother = models.IntegerField(verbose_name="Проживает с отчимом/мачехой совместно/раздельно",
                                                         blank=True, null=True)
    stepfather_stepmother_marriage_father = models.IntegerField(verbose_name="Проживает с отчимом/мачехой совместно/раздельно",
                                                         blank=True, null=True)
    mother_father_data = models.IntegerField(verbose_name="Сведениями о родителях распологаю/не распологаю",
                                             blank=True, null=True)
    guardians = models.ManyToManyField(Guardian, verbose_name="Опекуны", blank=True)
    guardians_other = models.CharField(max_length=255, verbose_name="Опекуны (иное)", blank=True, null=True)
    father_stepfather = models.TextField(verbose_name="Отец, отчим (данные)")
    mother_stepmother = models.TextField(verbose_name="Мать, мачеха (данные)")
    siblings = models.TextField(verbose_name="Братья (данные)")
    sport_kind = models.CharField(max_length=255, verbose_name="Вид спорта", blank=True, null=True)
    sport_level = models.IntegerField(verbose_name="Спортивный уровень", blank=True, null=True, default=1)
    sport_period = models.IntegerField(verbose_name="Периодичность занятий спортом", blank=True, null=True)
    sport_achievements = models.TextField(verbose_name="Спортивные достижения", blank=True, null=True)
    sport_is_only_by_program = models.BooleanField(verbose_name="Занимался спортом только по учебноей программе")
    interest = models.TextField(verbose_name="Ваши увлечения на данный момент")
    is_satisfied_with_the_training = models.ForeignKey(SatisfiedWithTheTraining, on_delete=models.CASCADE,
                                                       verbose_name="Удовлетворены ли Вы тем как проходило Ваше обучение", default=1)
    expectations = models.ForeignKey(Expectations, on_delete=models.CASCADE, verbose_name="Оправдались ожидания", default=1)
    character_change = models.ForeignKey(CharacterChange, on_delete=models.CASCADE, verbose_name="Как изменился характер", default=1)
    traits_formed = models.TextField(verbose_name="Какие качества сформировались")
    would_advise = models.IntegerField(verbose_name="Посоветовали бы поступать в Академию", default=1)
    after_graduating = models.ForeignKey(AfterGraduating, on_delete=models.CASCADE,
                                         verbose_name="Действия после окончания Академии", default=1)
    what_induce_to_quit = models.ManyToManyField(WhatInduceToQuit, verbose_name="Что может побудить Вас уволиться?", blank=True)
    what_induce_to_quit_other = models.CharField(max_length=255, verbose_name="Что может побудить Вас уволиться? (иное)", blank=True, null=True)
    what_keeps = models.ManyToManyField(WhatKeeps, verbose_name="Что Вас удерживает или мотивирует продолжать службу?", blank=True)

    what_keeps_other = models.CharField(max_length=255, verbose_name="Что Вас удерживает или мотивирует продолжать службу? (иное)", blank=True, null=True)
    how_did_teachers_influence = models.ForeignKey(HowDidTeachersInfluence, on_delete=models.CASCADE,
                                         verbose_name="Как в целом повлияли на ваше профессиональное становление преподаватели Академии МВД?", default=1)
    how_did_teachers_influence_explain = models.CharField(max_length=255,
                                                          verbose_name="Как в целом повлияли на ваше профессиональное становление преподаватели Академии МВД? (поясните ответ)")
    how_did_leaders_influence = models.ForeignKey(HowDidLeadersInfluence, on_delete=models.CASCADE,
                                         verbose_name="Как в целом повлияли на ваше профессиональное становление курсовые офицеры?", default=1)
    how_did_leaders_influence_explain = models.CharField(max_length=255,
                                                         verbose_name="Как в целом повлияли на ваше профессиональное становление курсовые офицеры? (поясните ответ)")
    need_conversation = models.IntegerField(verbose_name="Необходимость беседы с психологом", default=1)
    need_conversation_theme = models.TextField(verbose_name="Что обсудить с психологом", blank=True, null=True)
    i_inform = models.ManyToManyField(Inform, verbose_name="Я информирован", blank=True)
    fill_date_time = models.DateTimeField(auto_now=True, verbose_name="Дата заполнения")

    def __str__(self):
        return self.fio + ' ' + str(self.fill_date_time)

    @property
    def get_marital_status(self):
        if self.marital_status == 1:
            status = 'Холост/не замужем'
        elif self.marital_status == 2:
            status = 'Женат/замужем с ' + str(self.married_from)
        elif self.marital_status == 3:
            status = 'Разведен(а)'
        else:
            status = ''
        return status

    @property
    def get_has_children(self):
        if self.has_children == 0:
            has_children = 'Нет'
        elif self.has_children == 1:
            has_children = 'Да ' + str(self.children_data)
        else:
            has_children = ''
        return has_children

    @property
    def get_parents_data(self):
        parents_data = ''
        if self.parents_data == 1:
            parents_data = 'Мать и отец родные, состоят в браке, проживают совместно'
        elif self.parents_data == 2:
            parents_data = 'Мать и отец родные, находятся в разводе c ' + str(self.divorced_from)
            if self.divorced_live == 1:
                parents_data = parents_data + ', проживают раздельно'
            elif self.divorced_live == 2:
                parents_data = parents_data + ', проживают совместно'
        elif self.parents_data == 3:
            parents_data = 'Только мать, так как отец умер (погиб)'
            if self.mother_only_father_died_in:
                parents_data = parents_data + ' в ' + str(self.mother_only_father_died_in)
            elif self.mother_only_father_died_other:
                parents_data = parents_data + ' иное - ' + str(self.mother_only_father_died_other)
        elif self.parents_data == 4:
            parents_data = 'Только отец, мать умерла (погибла)'
            if self.father_only_mother_died_in:
                parents_data = parents_data + ' в ' + str(self.father_only_mother_died_in)
            elif self.father_only_mother_died_other:
                parents_data = parents_data + ' иное - ' + str(self.father_only_mother_died_other)
        elif self.parents_data == 5:
            parents_data = 'Родная мать проживает совместно с отчимом '
            if self.stepfather_stepmother_marriage_mother == 1:
                parents_data = parents_data + 'в браке'
            elif self.stepfather_stepmother_marriage_mother == 2:
                parents_data = parents_data + 'без регистрации брака'
        elif self.parents_data == 6:
            parents_data = 'Родной отец, проживает совместно с мачехой '
            if self.stepfather_stepmother_marriage_father == 1:
                parents_data = parents_data + 'в браке'
            elif self.stepfather_stepmother_marriage_father == 2:
                parents_data = parents_data + 'без регистрации брака'
        elif self.parents_data == 7:
            mother_father_list = ['матери', 'отце', 'обоих']
            parents_data = 'Сведениями о '
            parents_data = parents_data + mother_father_list[self.mother_father_data]
            parents_data = parents_data + ' не располагаю'
        elif self.parents_data == 8:
            parents_data = 'Опекуны - '
            for guardian in self.guardians.all():
                parents_data += guardian.guardian
                parents_data += ', '
            if self.guardians_other:
                parents_data = parents_data + self.guardians_other
        elif self.parents_data == 9:
            parents_data = 'Приемные родители'
        elif self.parents_data == 10:
            parents_data = 'Воспитанник детского дома'
        else:
            parents_data = 'Нет данных'
        return parents_data

    @property
    def get_sport_level(self):
        sport_levels = ['на любительском уровне', 'профессионально']
        if self.sport_kind:
            sport_level = sport_levels[self.sport_level-1]
        else:
            sport_level = ''
        return sport_level

    @property
    def get_sport_period(self):
        if self.sport_kind:
            return str(self.sport_period) + ' раз в неделю'
        else:
            return ''

    @property
    def get_sport_achievements(self):
        if self.sport_kind:
            return self.sport_achievements
        else:
            return ''

    @property
    def get_would_advise(self):
        advise_list = ['Да', 'Нет', 'Не знаю']
        return advise_list[self.would_advise-1]

    @property
    def get_need_conversation(self):
        needs_list = ['В беседе не нуждаюсь', 'Хотелось бы побеседовать (укажите, что конкретно Вы хотели бы обсудить)']
        return needs_list[self.need_conversation-1]






    class Meta:
        ordering = ('id',)
        verbose_name = 'Анкета выпускника'
        verbose_name_plural = 'Анкеты выпускников'