# -*- coding: utf-8 -*-

urlpatterns = patterns('django.views.generic',
    url(r'^$', 'simple.direct_to_template',
        kwargs={
            'template': 'index.html',
            'extra_context': {'item_list': lambda: Album.objects.all()}
        },
        name='index'
    ),
    url(r'^items/$', 'list_detail.object_list',
        kwargs={
            'queryset': Album.objects.all(),
            'template_name': 'items_list.html',
            'allow_empty': True
        },
        name='item_list'
    ),
    url(r'^items/(?P<object_id>\d+)/$', 'list_detail.object_detail',
        kwargs={
            'queryset': Album.objects.all(),
            'template_name': 'items_detail.html'
        },
        name='item_detail'
    ),
    url(r'^photos/(?P<object_id>\d+)/$', 'list_detail.object_detail',
        kwargs={
            'queryset': Photo.objects.all(),
            'template_name': 'photos_detail.html'
        },
        name='photo_detail'
    ),
)
