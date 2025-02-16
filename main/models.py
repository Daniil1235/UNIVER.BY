from django.db import models
from django.contrib.auth.models import AbstractUser
from premium.models import License


def profile_photo_path(instance, filename):
    if os.path.exists(f"mian/static/main/img/prof_photos/{instance.name}.jpg"):
        os.remove(f"mian/static/main/img/prof_photos/{instance.name}.jpg")
    return f"mian/static/main/img/prof_photos/{instance.name}.jpg"


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class User(AbstractUser):
    licensed = models.BooleanField('Лицензирован', default=False)
    license_key = models.ForeignKey(License, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name="Ключ лицензии")
    photo = models.ImageField("Фото профиля", upload_to=profile_photo_path, null=True, blank=True)
    user_type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Тип пользователя")

