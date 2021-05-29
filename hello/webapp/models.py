from django.contrib.auth import get_user_model
from django.db import models


STATUS_CHOICES = [('PUBLIC', 'public'), ('PRIVATE', 'private')]

class Photo(models.Model):
    the_photo = models.ImageField(null=False, blank=False, verbose_name='Фотогафия', upload_to='user_pics')
    signature = models.CharField(null=False, blank=True, max_length=100, verbose_name="Подпись")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, related_name='photo')
    choice = models.CharField(max_length=20, choices=STATUS_CHOICES, null=False, blank=False,
                              default='public', verbose_name="статус")
    album = models.ForeignKey("webapp.Album", related_name="AlbumPhoto", on_delete=models.CASCADE, verbose_name="album",
                              null=True, blank=True)

    class Meta:
        db_table = "Photo"
        verbose_name = "Фото"
        verbose_name_plural = "Фотки"

    def __str__(self):
        return f'{self.the_photo}, {self.signature}, {self.created_at}, {self.author}, {self.choice}, {self.album}'

class Album(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100, verbose_name="название")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='описание')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False, blank=False,
                               related_name='album')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    choice = models.CharField(max_length=20, choices=STATUS_CHOICES, null=False, blank=False,
                              default='public', verbose_name="статус")

    class Meta:
        db_table = "Album"
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    def __str__(self):
        return f'{self.name}, {self.description}, {self.created_at}, {self.author}, {self.choice}'

class Chosen (models.Model):
    photo_id = models.ForeignKey('webapp.Photo', related_name='ChosenPhoto', verbose_name="Выбраное фото",
                                 on_delete=models.CASCADE)
    user_id = models.ForeignKey(get_user_model(), related_name='ChosenUser', verbose_name="Этот пользователь",
                                on_delete=models.CASCADE)

