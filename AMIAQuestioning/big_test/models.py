from django.db import models
from course.models import Group


class TestKind(models.Model):
    kind = models.CharField(max_length=255, verbose_name="Вид теста")

    def __str__(self):
        return self.kind

    class Meta:
        ordering = ('kind',)
        verbose_name = 'Вид теста'
        verbose_name_plural = 'Виды тестов'


class Question(models.Model):
    question_number = models.IntegerField(verbose_name='Номер вопроса', blank=True, null=True)
    question_text = models.CharField(max_length=255, verbose_name='Вопрос')

    def __str__(self):
        return 'Номер вопроса ' + str(self.question_number) + ' Тест вопроса - ' + self.question_text

    class Meta:
        ordering = ('id',)
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Questionary(models.Model):
    fio = models.CharField(max_length=255, verbose_name='Фамилия')
    # group = models.CharField(max_length=255, verbose_name='Группа')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    kind = models.ForeignKey(TestKind, on_delete=models.SET_NULL, verbose_name="Вид теста", blank=True, null=True)
    date_of_birth = models.CharField(max_length=255, verbose_name='Дата рождения', blank=True, null=True)
    date_of_fill = models.DateField(verbose_name="Дата заполнения", auto_now_add=True)
    timer = models.IntegerField(verbose_name="Таймер", blank=True, null=True)

    def __str__(self):
        return self.fio + ' ' + str(self.date_of_fill)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'


class Result(models.Model):
    questionary = models.ForeignKey(Questionary, on_delete=models.CASCADE, verbose_name="Анкета")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")
    answer = models.IntegerField(verbose_name="Ответ")

    def __str__(self):
        return self.questionary.fio + ' ' + self.question.question_text + ' ' + str(self.answer)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
