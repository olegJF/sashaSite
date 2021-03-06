# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^(?P<page_number>\d+)/$', views.gallery, name='gallery'),
    url(r'^$', views.gallery, name='gallery'),
    # ex: /polls/5/
    #url(r'^([0-9]+)/(\d+)/$', views.album, name='album'),
    url(r'^(?P<page_number>\d+)/album/(?P<object_id>\d+)/$', views.album, name='album'),
    #url(r'^album/(?P<object_id>\d]+)/$', views.album, name='album'),
    #url(r'^album/([0-9]+)/$', views.album, name='album'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]


