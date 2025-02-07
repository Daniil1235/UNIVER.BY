from django.db import models
import random

from django.db.models.fields import DateField


class TimeLimit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Срок"
        verbose_name_plural = "Сроки"


class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "План"
        verbose_name_plural = "Планы"



class License(models.Model):
    id = models.AutoField(primary_key=True)
    time_limit = models.ForeignKey(TimeLimit, on_delete=models.CASCADE, verbose_name="Лимит")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name="План")
    key = models.CharField(max_length=100, verbose_name="Ключ")
    expire_date = DateField("Дата окончания", null=True, blank=True)

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = "Лицензия"
        verbose_name_plural = "Лицензии"
