from django.db import models
from django.contrib.auth.models import AbstractUser
from premium.models import License


class User(AbstractUser):
    licensed = models.BooleanField('Лицензирован', default=False)
    license_key = models.ForeignKey(License, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name="Ключ лицензии")

