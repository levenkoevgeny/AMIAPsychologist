from django.db import models


class Interest(models.Model):
    interest = models.CharField(verbose_name="В интересах", max_length=255)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Вопрос 04 - Поступил в интересах'
        verbose_name_plural = 'Вопрос 04 - Поступил в интересах'

    def __str__(self):
        return self.interest


class Educational(models.Model):
    educational = models.CharField(verbose_name="Название учебного учреждения", max_length=255)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Вопрос 05 - Окончил учебное учреждение'
        verbose_name_plural = 'Вопрос 05 - Окончил учебное учреждение'

    def __str__(self):
        return self.educational


class EducationalPlace(models.Model):
    educational_place = models.CharField(verbose_name="Расположение учебного учреждения (город)", max_length=255)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Вопрос 07 - Расположение учебного учреждения'
        verbose_name_plural = 'Вопрос 07 - Расположения учебных учреждений'

    def __str__(self):
        return self.educational_place


class LivePlaceRegion(models.Model):
    educational_place_region = models.CharField(verbose_name="Область фактического проживания",
                                                max_length=255)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Вопрос 08 - Область фактического проживания'
        verbose_name_plural = 'Вопрос 08 - Области фактического проживания'

    def __str__(self):
        return self.educational_place_region


class AttendExtra(models.Model):
    extra = models.CharField(verbose_name="Дополнительно посещал", max_length=255)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Вопрос 11 - Дополнительно посещал'
        verbose_name_plural = 'Вопрос 11 - Дополнительно посещал'

    def __str__(self):
        return self.extra


class ImportantFor(models.Model):
    important = models.CharField(verbose_name="Важно для поступающего при выборе УО", max_length=255)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Вопрос 12 - Важно для поступающего при выборе УО'
        verbose_name_plural = 'Вопрос 12 - Важно для поступающего при выборе УО'

    def __str__(self):
        return self.important


class ImportantForSpec(models.Model):
    important = models.CharField(verbose_name="Важно для поступающего обучаться по специальности", max_length=255)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Вопрос 13 - Важно для поступающего обучаться по специальности'
        verbose_name_plural = 'Вопрос 13 - Важно для поступающего обучаться по специальности'

    def __str__(self):
        return self.important


class GotInformationFrom(models.Model):
    got_from = models.CharField(verbose_name="Источник информации", max_length=255)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Вопрос 14 - Информацию о поступлении получил'
        verbose_name_plural = 'Вопрос 14 - Информацию о поступлении получил'

    def __str__(self):
        return self.got_from


class Decision(models.Model):
    decision = models.CharField(verbose_name="Решение было принято", max_length=255)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Вопрос 15 - Решение было принято'
        verbose_name_plural = 'Вопрос 15 - Решение было принято'

    def __str__(self):
        return self.decision


class LetYou(models.Model):
    let_you = models.CharField(verbose_name="Поступление позволит", max_length=255)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Вопрос 16 - Поступление позволит'
        verbose_name_plural = 'Вопрос 16 - Поступление позволит'

    def __str__(self):
        return self.let_you


class Difficulty(models.Model):
    difficulty = models.CharField(verbose_name="Трудность при оформлении личного дела", max_length=255)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Вопрос 17 - Трудность при оформлении личного дела'
        verbose_name_plural = 'Вопрос 17 - Трудность при оформлении личного дела'

    def __str__(self):
        return self.difficulty


class GetEducation(models.Model):
    get_education = models.TextField(verbose_name="При обучении получение какого высшего образования для Вас важно",
                                     max_length=255)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'Вопрос 18 - При обучении получение какого высшего образования для Вас важноа'
        verbose_name_plural = 'Вопрос 18 - При обучении получение какого высшего образования для Вас важно'

    def __str__(self):
        return self.get_education


class Questionary(models.Model):
    sex = models.IntegerField(verbose_name="Ваш пол", default=1)
    year_of_birth = models.IntegerField(verbose_name="Год рождения")
    year_count = models.IntegerField(verbose_name="Полных лет")
    in_the_interests_of = models.ForeignKey(Interest, on_delete=models.CASCADE,
                                            verbose_name="На учебу в Академию МВД Вы направляетесь в интересах", default=1)
    in_the_interests_of_other = models.CharField(max_length=255,
                                                 verbose_name="На учебу в Академию МВД Вы направляетесь (иное)",
                                                 blank=True, null=True)
    graduate = models.ForeignKey(Educational, on_delete=models.CASCADE, verbose_name="Какое учебное заведение Вы заканчивали?",
                                 default=1)
    is_law_orientation = models.IntegerField(verbose_name="Обучались ли Вы в классе правовой направленности?", default=1)
    place_of_last_education = models.ForeignKey(EducationalPlace, on_delete=models.CASCADE,
                                                verbose_name="Последнее учебное заведение, которое Вы оканчивали, находится в",
                                                default=1)
    # place_of_last_education_other_city = models.CharField(verbose_name="Иное расположение учебного учреждения (город)",
    #                                                       max_length=255, blank=True, null=True)
    live_region = models.ForeignKey(LivePlaceRegion, on_delete=models.CASCADE,
                                    verbose_name="Область в которой Вы фактически проживаете",
                                    default=1)
    average_mark = models.FloatField(verbose_name="Средний балл по аттестату, диплому")
    mark_sum = models.IntegerField(verbose_name="Сумма баллов по ЦТ (если сдавали)", blank=True, null=True)
    attend_extra = models.ManyToManyField(AttendExtra,
                                          verbose_name="Перед поступлением в Академию МВД Вы дополнительно посещали")
    important_for = models.ManyToManyField(ImportantFor, verbose_name="При выборе высшего УО важно")
    important_for_other = models.CharField(max_length=255,
                                           verbose_name="При выборе высшего УО важно (иное)",
                                           blank=True, null=True)
    important_for_spec = models.ManyToManyField(ImportantForSpec,
                                                verbose_name="Важно поступить и обучаться по специальности")
    got_information_from = models.ManyToManyField(GotInformationFrom,
                                                  verbose_name="Информацию о поступлении в Академия получил")
    got_information_from_other = models.CharField(max_length=255,
                                                  verbose_name="Информацию о поступлении в Академия получил (иное)",
                                                  blank=True, null=True)
    decision = models.ForeignKey(Decision, on_delete=models.CASCADE,
                                 verbose_name="Решение о поступлении на обучение было принято", default=1)
    decision_other = models.CharField(max_length=255,
                                      verbose_name="Решение о поступлении на обучение было принято (иное)",
                                      blank=True, null=True)
    let_you = models.ManyToManyField(LetYou,
                                     verbose_name="Поступление Вам позволит")

    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE,
                                   verbose_name="Основная трудность при оформлении личного дела", default=1)
    get_education = models.ForeignKey(GetEducation, on_delete=models.CASCADE,
                                      verbose_name="Получение какого образования важно", default=1)
    time_added = models.DateTimeField(verbose_name="Дата и время заполнения анкеты", blank=True, null=True)

    @property
    def year_time_added(self):
        return self.time_added.strftime('%Y')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'

    def __str__(self):
        return str(self.id)


