import os
from runtext.models import Message
from django.shortcuts import render
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from runtext.utils import create_scrolling_text_video

OUTPUT_NAME = 'media/my_video.mp4'


def index(request):
    text = request.GET['text']

    Message.objects.create(msg=text)

    create_scrolling_text_video(text, OUTPUT_NAME)
    file = FileWrapper(open(OUTPUT_NAME, 'rb'))
    response = HttpResponse(file, content_type='video/mp4')
    response['Content-Disposition'] = 'attachment; filename=my_video.mp4'

    return response
