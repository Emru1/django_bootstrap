import uuid

from django.db import models
from django.utils import timezone


class Gallery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(verbose_name='Nazwa', max_length=64)
    desc = models.CharField(verbose_name='Opis', max_length=1024)
    date = models.DateTimeField(
        verbose_name='Czas wrzucenia',
        default=timezone.now,
        editable=False,
    )

    def __str__(self) -> str:
        return str(self.name)


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(verbose_name='Nazwa', max_length=64)
    desc = models.CharField(verbose_name='Opis', max_length=1024)
    fs_file = models.ImageField()
    date = models.DateTimeField(
        verbose_name='Czas wrzucenia',
        default=timezone.now,
        editable=False,
    )
    gallery = models.ForeignKey(
        Gallery,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name='images_rel',
    )

    def __str__(self) -> str:
        return str(self.name)


class GalleryComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.CharField(max_length=1024)
    date = models.DateTimeField(
        verbose_name='Czas wrzucenia',
        default=timezone.now,
        editable=False,
    )
    gallery = models.ForeignKey(
        Gallery,
        verbose_name='Galeria',
        on_delete=models.CASCADE,
        related_name='comments_rel',
    )


class ImageComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    text = models.CharField(max_length=1024)
    date = models.DateTimeField(
        verbose_name='Czas wrzucenia',
        default=timezone.now,
        editable=False,
    )
    image = models.ForeignKey(
        Image,
        verbose_name='Zdjęcie',
        on_delete=models.CASCADE,
        related_name='comments_rel',
    )
