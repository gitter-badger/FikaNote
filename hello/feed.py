#!/usr/bin/env python
#coding:utf-8
import requests
from django.http import HttpResponse
from .models import FikanoteDB
from django.utils import feedgenerator

def feed(request):
    feed=feedgenerator.Rss201rev2Feed(
        title='FikaNote'
        , link='https://fikanote.herokuapp.com/'
        , description='Talking about Tech, Software Development and Gadgets with Coffee.'
        , language='ja-jp'
        )

    episodes = FikanoteDB.objects.order_by('-date')
    for episode in episodes:
        url = 'https://fikanote.herokuapp.com/%d/' % episode.number
        feed.add_item(
            title=episode.title
            , link=url
            , description=episode.agenda
            , pubdate=episode.date
            )

    result=feed.writeString('utf-8')
    return HttpResponse(result, content_type="text/xml; charset=utf-8")


