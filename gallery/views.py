# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response, render
from gallery.models import Album, Photo
#from django.http import HttpResponse, request


# Create your views here.
def gallery(request):
    item_list = Album.objects.all()
    return render(request, 'gallery/index.tpl', {'item_list':item_list})

def album(request, object_id):
    photos_list = Album.objects.get( pk=object_id)
    count = photos_list.photo_set.count()

    context = dict()
    context['object'] = photos_list
    photos_rows = []
    more_one_line = False
    #photo_last_line = False
    #photo_in_last_line = []
    photo_in_row = 3
    if count > photo_in_row:
        cnt = count/photo_in_row
        more_one_line = True
        for i in range(1, cnt+1):
            photos_rows.append(i*photo_in_row)


        #if count%photo_in_row:
        #   photo_last_line=True
        #   for i in range(cnt*photo_in_row, count):
        #       photo_in_last_line.append(i+1)
    context['photos_rows'] = photos_rows
    context['more_one_line'] = more_one_line
    #context['photo_last_line'] = photo_last_line
    #context['photo_in_last_line'] = photo_in_last_line


    return render(request, 'gallery/album.tpl', context)
