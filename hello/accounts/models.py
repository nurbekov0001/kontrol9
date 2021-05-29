from django.db import models

from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Ползователь')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Полное описание")

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        permissions = [('view_users', 'Просмотр пользоватей')]

# Create your models here.
