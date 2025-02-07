import os
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Country(models.Model):
    name = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Subject(models.Model):
    name = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"



class Direction(models.Model):
    name = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


def univer_photo_path(instance, filename):
    if os.path.exists(f"univers/static/univers/img/photos/{instance.name}.jpg"):
        os.remove(f"univers/static/univers/img/photos/{instance.name}.jpg")
    return f"univers/static/univers/img/photos/{instance.name}.jpg"


# noinspection LongLine
class Univer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание", help_text="Описание универа, важной информации о нём")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Страна")
    address = models.CharField("Адрес", max_length=150)
    number = models.CharField("Номер телефона", max_length=50, help_text="Введите номер телефона в формате +XXX (XX) XXX-XX-XX")
    email = models.CharField("email", max_length=150, blank=True, null=True)
    photo = models.ImageField("Фото", upload_to=univer_photo_path)
    website = models.CharField("Оффициальный сайт", max_length=150)

    twitter = models.CharField("twitter", max_length=150, blank=True, null=True)
    facebook = models.CharField("facebook", max_length=150, blank=True, null=True)
    linkedin = models.CharField("linkedin", max_length=150, blank=True, null=True)
    instagram = models.CharField("instagram", max_length=150, blank=True, null=True)
    youtube = models.CharField("youtube", max_length=150, blank=True, null=True)
    telegram = models.CharField("telegram", max_length=150, blank=True, null=True)

    subjects = models.ManyToManyField(Subject, verbose_name="Предметы")
    directions = models.ManyToManyField(Direction, verbose_name="Направления")

    bysite = models.BooleanField("Программы от нас", default=False)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Универ"
        verbose_name_plural = "Универы"



@receiver(pre_delete, sender=Univer)
def univer_delete(sender, instance, **kwargs):
    instance.photo.delete(False)