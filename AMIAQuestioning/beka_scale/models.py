from django.db import models


class Question(models.Model):
    question_number = models.IntegerField(verbose_name='Номер вопроса', blank=True, null=True)
    question_text = models.CharField(max_length=255, verbose_name='Вопрос')

    def __str__(self):
        return 'Номер вопроса ' + str(self.question_number) + ' Тест вопроса - ' + self.question_text

    class Meta:
        ordering = ('id',)
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Position(models.Model):
    position = models.CharField(max_length=255, verbose_name='Должность')

    def __str__(self):
        return self.position

    class Meta:
        ordering = ('id',)
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class BekaScale(models.Model):
    fio = models.CharField(max_length=255, verbose_name='Фамилия')
    group = models.CharField(max_length=255, verbose_name='Группа')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность')
    date_of_fill = models.DateField(verbose_name="Дата заполнения", auto_now_add=True)

    def __str__(self):
        return self.fio + ' ' + str(self.date_of_fill)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'


class Result(models.Model):
    beka_scale = models.ForeignKey(BekaScale, on_delete=models.CASCADE, verbose_name="Анкета")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")
    answer = models.IntegerField(verbose_name="Ответ")

    def __str__(self):
        return self.beka_scale.fio + ' ' + self.question.question_text + ' ' + str(self.answer)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
