from django.db import models
import random


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


def gener_key():
    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    key = ""
    for i in range(5):
        if i != 0:
            key += "-"
        for q in range(5):
            ltype = random.randint(0, 1)
            if ltype:
                key += random.choice(digits)
            else:
                key += random.choice(letters)
    return key




class License(models.Model):
    id = models.AutoField(primary_key=True)
    time_limit = models.ForeignKey(TimeLimit, on_delete=models.CASCADE, verbose_name="Лимит")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name="План")
    key = models.CharField(max_length=100, verbose_name="Ключ", blank=True, default=gener_key())

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = "Лицензия"
        verbose_name_plural = "Лицензии"
