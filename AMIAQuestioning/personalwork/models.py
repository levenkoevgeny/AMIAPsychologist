from django.db import models
from django.contrib.auth.models import User


class Rank(models.Model):
    rank_title = models.CharField(max_length=255, verbose_name="Звание")

    def __str__(self):
        return self.rank_title

    class Meta:
        ordering = ('rank_title',)
        verbose_name = 'Звание'
        verbose_name_plural = 'Звания'


class Subdivision(models.Model):
    subdivision_title = models.CharField(max_length=255, verbose_name="Подразделение")

    def __str__(self):
        return self.subdivision_title

    class Meta:
        ordering = ('subdivision_title',)
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class WorkKind(models.Model):
    work_kind = models.CharField(max_length=255, verbose_name="Вид работы")

    def __str__(self):
        return self.work_kind

    class Meta:
        ordering = ('work_kind',)
        verbose_name = 'Вид работы'
        verbose_name_plural = 'Виды работы'


class Request(models.Model):
    work_request = models.CharField(max_length=255, verbose_name="Запрос")

    def __str__(self):
        return self.work_request

    class Meta:
        ordering = ('work_request',)
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'


class WorkDone(models.Model):
    work_done = models.CharField(max_length=255, verbose_name="Основание и проведенная работа")

    def __str__(self):
        return self.work_done

    class Meta:
        ordering = ('work_done',)
        verbose_name = 'Основание и проведенная работа'
        verbose_name_plural = 'Основания и проведенные работы'


class PersonalWork(models.Model):
    lastname = models.CharField(max_length=255, verbose_name="Фамилия и инициалы")
    work_date = models.DateField(verbose_name="Дата")
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, verbose_name="Звание", blank=True, null=True)
    subdivision = models.ForeignKey(Subdivision, verbose_name="Подразделение", on_delete=models.CASCADE)
    work_kind = models.ForeignKey(WorkKind, verbose_name="Вид работы", on_delete=models.CASCADE)
    work_request = models.ForeignKey(Request, verbose_name="Запрос", on_delete=models.CASCADE)
    work_done = models.ForeignKey(WorkDone, verbose_name="Основание и проведеннная работа", on_delete=models.CASCADE)
    conclusion = models.TextField(verbose_name="Выводы", blank=True, null=True)
    recommendations = models.TextField(verbose_name="Рекомендации", blank=True, null=True)
    executor = models.ForeignKey(User, verbose_name="Исполнитель", on_delete=models.CASCADE)
    add_date_time = models.DateTimeField(verbose_name="Дата и время добавления записи", auto_now_add=True)
    last_modification = models.DateTimeField(verbose_name="Дата и время последнего редактирования", auto_now=True)
    extra_data = models.TextField(verbose_name="Дополнительная информация", blank=True, null=True)

    def __str__(self):
        return self.lastname + ' исполнитель - ' + str(self.executor)

    class Meta:
        ordering = ('-work_date', '-id')
        verbose_name = 'Индивидуальная работа'
        verbose_name_plural = 'Индивидуальные работы'