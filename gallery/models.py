# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import permalink
from gallery.fields import ThumbnailImageField


class Album(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название альбома транслитом')
    title = models.CharField(max_length=50, verbose_name='Название альбома')
    description = models.TextField(blank=True, verbose_name='Описание альбома')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'альбомы'
        ordering = ['name']



    def __unicode__(self):
        return self.name


    def get_absolute_url(self):
        return ('item_detail', None, {'object_id': self.id})

class Photo (models.Model):
    item = models.ForeignKey(Album)
    title = models.CharField(max_length=100, verbose_name='Название фото')
    image = ThumbnailImageField(upload_to='static/photos')
    caption = models.TextField(blank=True, verbose_name='Описание фото')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'фотографии'
        ordering = ['title']

    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('album', args=[str(self.id)])
