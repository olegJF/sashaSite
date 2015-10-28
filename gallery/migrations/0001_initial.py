# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gallery.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb0\xd0\xbb\xd1\x8c\xd0\xb1\xd0\xbe\xd0\xbc\xd0\xb0 \xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd1\x81\xd0\xbb\xd0\xb8\xd1\x82\xd0\xbe\xd0\xbc')),
                ('title', models.CharField(max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb0\xd0\xbb\xd1\x8c\xd0\xb1\xd0\xbe\xd0\xbc\xd0\xb0')),
                ('description', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb0\xd0\xbb\xd1\x8c\xd0\xb1\xd0\xbe\xd0\xbc\xd0\xb0', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u0410\u043b\u044c\u0431\u043e\u043c',
                'verbose_name_plural': '\u0430\u043b\u044c\u0431\u043e\u043c\u044b',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x84\xd0\xbe\xd1\x82\xd0\xbe')),
                ('image', gallery.fields.ThumbnailImageField(upload_to=b'static/photos')),
                ('caption', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x84\xd0\xbe\xd1\x82\xd0\xbe', blank=True)),
                ('item', models.ForeignKey(to='gallery.Album')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f',
                'verbose_name_plural': '\u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438',
            },
        ),
    ]
